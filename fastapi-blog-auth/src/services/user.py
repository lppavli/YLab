from functools import lru_cache
from typing import Optional

import jwt
from fastapi import Depends
from sqlmodel import Session
from werkzeug.security import generate_password_hash, check_password_hash
from src.api.v1.schemas.users import UserCreate, UserLogin, UserAbout, UserUpdate
from src.core.auth_config import blocked_access_tokens, settings, active_refresh_tokens

from src.core.config import JWT_ALGORITHM, JWT_SECRET_KEY
from src.db import AbstractCache, get_cache, get_session
from src.models import User
from src.services import ServiceMixin

__all__ = ("UserService", "get_user_service")


class UserService(ServiceMixin):
    def create_user(self, user: UserCreate) -> dict:
        """Зарегистрировать пользователя"""
        new_user = User(
            username=user.username,
            password=generate_password_hash(user.password, method="sha256"),
            email=user.email,
        )
        if self.session.query(User).filter(User.username == new_user.username).first():
            return {"error": "User already exists."}
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return {"msg": "User created.", "user": new_user}

    def user_detail(self, jwt) -> Optional[dict]:
        """Информация об авторизованном пользователе"""
        jwt.jwt_required()
        current_user = jwt.get_jwt_subject()
        user_info = (
            self.session.query(User).filter(User.username == current_user).first()
        )
        res = UserAbout(
            uuid=user_info.uuid,
            username=user_info.username,
            password=user_info.password,
            email=user_info.email,
            created_at=user_info.created_at,
            is_superuser=user_info.is_superuser,
        )
        return {"user": res}

    def user_change(self, _jwt, user: UserUpdate):
        """Изменить информацию о пользователе"""
        _jwt.jwt_required()
        current_username = _jwt.get_jwt_subject()
        current_user = (
            self.session.query(User).filter(User.username == current_username).first()
        )
        if self.session.query(User).filter(User.username == user.username).first():
            return {"error": "User already exists."}
        for key, value in user.dict().items():
            setattr(current_user, key, value)
        res = UserAbout(
            uuid=current_user.uuid,
            username=current_user.username,
            password=current_user.password,
            email=current_user.email,
            created_at=current_user.created_at,
            is_superuser=current_user.is_superuser,
        )
        self.session.add(current_user)
        self.session.commit()
        self.session.refresh(current_user)
        jti = _jwt.get_raw_jwt()["jti"]
        blocked_access_tokens.setex(jti, settings.access_expires, "true")
        access_token = _jwt.create_access_token(subject=user.username)
        return {"user": res, "access_token": access_token}

    def login(self, _jwt, user: UserLogin) -> dict:
        """Войти в аккаунт"""
        check_user = (
            self.session.query(User).filter(User.username == user.username).first()
        )
        if not check_user:
            return {"error": "User not exists."}
        if not check_password_hash(check_user.password, user.password):
            return {"error": "Password is invalid"}
        user_uuid = (
            self.session.query(User)
            .filter(User.username == check_user.username)
            .first()
            .uuid
        )
        access_token = _jwt.create_access_token(subject=user.username)
        refresh_token = _jwt.create_refresh_token(subject=user.username)
        active_refresh_tokens.sadd(user_uuid, refresh_token)
        return {"access_token": access_token, "refresh_token": refresh_token}

    def refresh(self, _jwt) -> dict:
        """Обновить токен"""
        _jwt.jwt_refresh_token_required()
        current_username = _jwt.get_jwt_subject()
        user_uuid = (
            self.session.query(User)
            .filter(User.username == current_username)
            .first()
            .uuid
        )
        payload = _jwt.get_raw_jwt()
        new_access_token = _jwt.create_access_token(subject=current_username)
        new_refresh_token = _jwt.create_refresh_token(subject=current_username)
        active_refresh_tokens.sadd(user_uuid, new_refresh_token)
        active_refresh_tokens.srem(user_uuid, get_token_from_payload(payload))
        return {"access_token": new_access_token, "refresh_token": new_refresh_token}

    def logout(self, _jwt):
        """Выйти из аккаунта"""
        _jwt.jwt_refresh_token_required()
        current_username = _jwt.get_jwt_subject()
        user_uuid = (
            self.session.query(User)
            .filter(User.username == current_username)
            .first()
            .uuid
        )
        payload = _jwt.get_raw_jwt()
        active_refresh_tokens.srem(user_uuid, get_token_from_payload(payload))
        return {"msg": "Successfully logout"}

    def logout_all(self, _jwt):
        """Выйти со всех устройств"""
        _jwt.jwt_refresh_token_required()
        current_username = _jwt.get_jwt_subject()
        user_uuid = (
            self.session.query(User)
            .filter(User.username == current_username)
            .first()
            .uuid
        )
        active_refresh_tokens.delete(user_uuid)
        return {"msg": "Successfully logout"}


def get_token_from_payload(payload: dict):
    return jwt.encode(payload, "secret", "HS256")


@lru_cache()
def get_user_service(
    cache: AbstractCache = Depends(get_cache),
    session: Session = Depends(get_session),
) -> UserService:
    return UserService(cache=cache, session=session)

import json

from redis import Redis
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


# обычный декоратор для кэширования
def cached(func):
    cache = {}

    def decorated_func(*args, **kwargs):
        nonlocal cache
        if args in cache:
            logging.info("Данные взяты из кэш")
            return cache[args]
        else:
            result = func(*args, **kwargs)
            cache[args] = result
            logging.info("Данные добавлены в кэш")
            return result

    return decorated_func


# декоратор в Redis
def redis_cache(func):
    redis = Redis()

    def decorated_func(*args, **kwargs):
        nonlocal redis
        key = " - ".join([str(arg) for arg in args])
        result = redis.get(key)
        if not result:
            result = func(*args, **kwargs)
            result_json = json.dumps(result)
            redis.set(key, result_json)
            logging.info("берем данные из функции")
        else:
            result_json = result.decode("utf-8")
            result = json.loads(result_json)
            logging.info("берем данные из кэш")
        return result

    redis.close()
    return decorated_func


@cached
def multiplier(number: int):
    return number * 2


@redis_cache
def multiplier_with_redis(number: int):
    return number * 2


if __name__ == "__main__":

    # Испытание простого кэширования
    print(multiplier(2))
    print(multiplier(2))
    print(multiplier(2))

    # Испытание redis-декоратора
    print(multiplier_with_redis(5))
    print(multiplier_with_redis(5))
    print(multiplier_with_redis(5))

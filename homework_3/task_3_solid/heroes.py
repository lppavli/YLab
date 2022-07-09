from abc import ABC, abstractmethod

from homework_3.task_3_solid.weapons import Gun, Laser, Karate


class SuperHero(ABC):
    @property
    def name(self):
        pass

    @property
    def can_use_ultimate_attack(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class Superman(SuperHero, Laser, Karate):
    name = "Clark Kent"
    can_use_ultimate_attack = True

    def attack(self):
        if self.can_use_ultimate_attack:
            self.incinerate_with_lasers()
        return self.roundhouse_kick()


class ChackNorris(SuperHero, Gun, Laser):
    name = "Chack Norris"
    can_use_ultimate_attack = False

    def attack(self):
        if self.can_use_ultimate_attack:
            self.incinerate_with_lasers()
        return self.fire_a_gun()

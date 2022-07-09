from abc import ABC, abstractmethod


class Place(ABC):
    @property
    def name(self):
        return "place"

    @abstractmethod
    def get_antagonist(self):
        pass


class Kostroma:
    name = "Kostroma"

    def get_antagonist(self):
        print("Orcs hid in the forest")


class Tokyo:
    name = "Tokyo"

    def get_antagonist(self):
        print("Godzilla stands near a skyscraper")

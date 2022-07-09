from abc import abstractmethod, ABC


class Media(ABC):
    @abstractmethod
    def create_news(self, text):
        pass


class NewsPaper(Media):
    def create_news(self, text):
        print(f"Print in the newspaper: {text}")


class TV(Media):
    def create_news(self, text):
        print(f"News on the TV: {text}")

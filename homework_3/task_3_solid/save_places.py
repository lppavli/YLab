from homework_3.task_3_solid.heroes import SuperHero
from homework_3.task_3_solid.news import Media
from homework_3.task_3_solid.places import Place


class SavePlace:
    def __init__(self, hero: SuperHero, place: Place, media: Media):
        self.hero = hero
        self.place = place
        self.media = media

    def find(self):
        return self.place.get_antagonist()

    def save_the_place(self):
        self.find()
        self.hero.attack()
        self.media.create_news(f"{self.hero.name} saved the {self.place.name}")

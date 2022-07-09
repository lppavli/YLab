from heroes import Superman, ChackNorris
from homework_3.task_3_solid.news import NewsPaper, TV
from homework_3.task_3_solid.save_places import SavePlace
from places import Kostroma, Tokyo


if __name__ == "__main__":
    s = SavePlace(Superman(), Kostroma(), NewsPaper())
    s.save_the_place()
    print("-" * 20)
    s = SavePlace(ChackNorris(), Tokyo(), TV())
    s.save_the_place()

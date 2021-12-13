
import curses, itertools
from time import sleep
from collections import defaultdict

from chronology import chronology_patterns
from models.lift import Lift
from models.view import View
from models.people import People


def run():
    """Fonction principale du projet.

    Boucle infinie qui incrémente un tick.
    Génère la vue sur le CMD
    Exécute l'étape suivante du l'ascenseur
    """
    lift = Lift(nbr_of_stage=9)
    view = View(lift)
    chronology = build_chronology(lift)
    try:
        screen = curses.initscr()
        for actual_tick in itertools.count(start=1):
            # Ajoute la ou les personnes prévues sur le tick actuel.
            if actual_tick in chronology:
                for people in chronology[actual_tick]:
                    lift.add_people(people)
                del chronology[actual_tick]
            statements = view.render(actual_tick)
            screen.clear()
            screen.addstr(1, 0, '\n'.join(statements))
            screen.refresh()
            lift.next()
            sleep(1)
    finally:
        curses.endwin()


def build_chronology(lift):
    """Construit la chronologie par rapport au pattern renseigné.
    """
    chronology = defaultdict(list)
    for id, values in chronology_patterns.items():
        if values["start"] == values["arrival"]:
            continue
        if values["start"] <= 0 or values["start"] > lift.nbr_of_stage:
            continue
        if values["arrival"] <= 0 or values["arrival"] > lift.nbr_of_stage:
            continue
        people = People(
                start=values["start"],
                arrival=values["arrival"],
                asked_at=values["tick"],
                id=id)
        chronology[values["tick"]].append(people)
    return chronology


run()

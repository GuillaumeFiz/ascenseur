

class Lift:

    def __init__(s, nbr_of_stage: int):
        s.nbr_of_stage = nbr_of_stage
        s.actual_stage = 1
        s.pause = True
        # Direction de l'ascenseur : to_bottom == False -> Descend
        #                            to_bottom == True -> Monte
        s.to_bottom = False
        s.target = None
        s.waiting = {}
        s.on_the_move = {}
        s.arrived = {}

    def next(s):
        """Réalise la prochaine étape de l'ascenseur
        """
        if s.need_new_target():
            s.select_target()
        if s.target_can_go_up():
            s.take_target()
        s.descents_of_people()
        s.bring_up_peoples_on_this_stage()
        if s.lift_can_move():
            s.move()
        else:
            s.pause = True

    def lift_can_move(s) -> bool:
        """Détermine si l'ascenseur peut bouger.

        Si il est vide et qu'il n'a aucune cible, celui-ci restera sur place.
        """
        return s.target is not None or len(s.on_the_move) > 0

    def move(s):
        """Détermine le mouvement que doit réaliser l'ascenseur.
        """
        s.actual_stage += -1 if s.to_bottom else 1

    def need_new_target(s) -> bool:
        """Vérifie si une nouvelle cible est nécessaire.

        Cette cible sera cherchée si l'ascenseur n'a pas de passagers à
        bord, qu'il n'a pas déjà une cible en cours et qu'au moins 1
        personne est en attente.
        """
        if len(s.on_the_move) > 0:
            return False
        if s.target is not None:
            return False
        if len(s.waiting) == 0:
            return False
        return True

    def select_target(s):
        """Retourne la prochaine cible après une pause de l'ascenseur.

        La cible sera la personne la plus ancienne qui a appelé l'ascenseur.
        En cas d'égalité d'ancienneté, la personne la plus proche de
        l'ascenseur sera privilégiée.
        """
        if len(s.waiting.values()) == 0:
            return
        s.target = list(s.waiting.values())[0]
        for people in list(s.waiting.values())[1:]:
            # Personne plus ancienne que la cible
            if s.target.asked_at > people.asked_at:
                s.target = people
            # Personne aussi ancienne mais plus proche
            elif s.target.asked_at == people.asked_at:
                distance_with_target = abs(s.target.start - s.actual_stage)
                new_distance = abs(people.start - s.actual_stage)
                if new_distance < distance_with_target:
                    s.target = people
        s.to_bottom = (s.target.start < s.actual_stage)
        s.pause = False

    def take_target(s):
        """Fait monter la cible et donne la bonne direction à l'ascenseur
        """
        s.on_the_move[s.target.id] = s.target
        s.to_bottom = (s.target.arrival < s.actual_stage)
        del s.waiting[s.target.id]
        s.target = None

    def target_can_go_up(s):
        """Vérifie si l'ascenseur est arrivé à l'étage de sa cible.
        """
        return s.target is not None and s.target.start == s.actual_stage

    def descents_of_people(s):
        """Fait sortir les personnes qui sont arrivées au bon étage.
        """
        for people in [p for p in s.on_the_move.values()]:
            if people.arrival == s.actual_stage:
                s.arrived[people.id] = people
                del s.on_the_move[people.id]

    def bring_up_peoples_on_this_stage(s):
        """Parcours l'ensemble des personnes en attente et vérifie si
        une ou plusieurs personnes sont autorisées à monter à bord.

        Une personne est autorisée si elle se trouve au même étage que
        l'ascenseur et qu'elle veut aller dans la même direction que lui.
        """
        for people in [p for p in s.waiting.values()]:
            if people.start != s.actual_stage:
                continue
            if people.want_to_go_down() and not s.to_bottom:
                continue
            if not people.want_to_go_down() and s.to_bottom:
                continue
            s.on_the_move[people.id] = people
            del s.waiting[people.id]

    def add_people(s, people):
        """Ajoute une personne à la liste des personnes en attentes.
        """
        s.waiting[people.id] = people

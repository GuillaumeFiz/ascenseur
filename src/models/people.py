

class People:

    def __init__(self, start: int, arrival: int, asked_at: int, id: str):
        self.start = start
        self.arrival = arrival
        self.asked_at = asked_at
        self.id = id
        self.is_arrived = False

    def want_to_go_down(self) -> bool:
        return self.start > self.arrival

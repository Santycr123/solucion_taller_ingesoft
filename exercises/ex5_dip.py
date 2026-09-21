"""
Exercise 5 - Dependency Inversion Principle (DIP)

Run this file directly to see the race:
    python -m exercises.ex5_dip
"""
from typing import List, Optional

from engine.track import Racer, Track


class SportsCar:
    symbol = "\U0001F3CE"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 6


class DeliveryVan:
    symbol = "\U0001F690"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 3


class RocketSled:
    symbol = "\U0001F680"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 9


class Race:
    """High-level policy: depends only on the Racer abstraction, injected
    from the outside. It has no idea what a SportsCar or a RocketSled is.
    """

    def __init__(self, racers: List[Racer], track: Optional[Track] = None):
        self.racers = racers
        self.track = track or Track(length=30)

    def start(self):
        return self.track.run(self.racers)


def main():
    roster_a = [SportsCar("Flash"), DeliveryVan("Steady Eddie")]
    Race(roster_a).start()

    roster_b = [RocketSled("Comet"), DeliveryVan("Steady Eddie II")]
    Race(roster_b).start()  # Race was never modified, only its input was.


if __name__ == "__main__":
    main()

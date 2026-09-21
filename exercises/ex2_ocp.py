"""
Exercise 2 - Open/Closed Principle (OCP)

Run this file directly to see the race:
    python -m exercises.ex2_ocp
"""
import random

from engine.track import Track


class Vehicle:
    """Base type every racer in this exercise extends."""

    symbol = "?"

    def __init__(self, name: str):
        self.name = name
        self.position = 0

    def move(self) -> None:
        raise NotImplementedError


class Car(Vehicle):
    symbol = "\U0001F697"

    def move(self) -> None:
        self.position += 4


class Truck(Vehicle):
    symbol = "\U0001F69A"

    def move(self) -> None:
        self.position += 2


class Motorcycle(Vehicle):
    symbol = "\U0001F3CD"

    def move(self) -> None:
        # Fast, but erratic: sometimes bursts, sometimes wobbles.
        self.position += random.choice([1, 2, 6, 7])


class Bicycle(Vehicle):
    symbol = "\U0001F6B2"

    def __init__(self, name: str):
        super().__init__(name)
        self._ticks = 0

    def move(self) -> None:
        # Starts strong, tires out over time.
        self._ticks += 1
        self.position += max(1, 5 - self._ticks // 3)


def main():
    vehicles = [
        Car("Red Car"),
        Truck("Big Rig"),
        Motorcycle("Ghost Rider"),
        Bicycle("Pedal Pete"),
    ]
    Track(length=35).run(vehicles)


if __name__ == "__main__":
    main()

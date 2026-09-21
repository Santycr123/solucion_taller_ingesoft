"""
Exercise 3 - Liskov Substitution Principle (LSP)

Run this file directly to see the race:
    python -m exercises.ex3_lsp
"""
import random

from engine.track import Track


class Vehicle:
    """Contract every vehicle here must honor:
    - move() must leave position >= its previous value (never backwards).
    - move() must never raise.
    Any subclass that cannot honor this contract must not be a Vehicle.
    """

    symbol = "?"

    def __init__(self, name: str):
        self.name = name
        self.position = 0

    def move(self) -> None:
        raise NotImplementedError


class SteadyCar(Vehicle):
    symbol = "\U0001F697"

    def move(self) -> None:
        self.position += 4


class UnreliableCar(Vehicle):
    """Sometimes stalls (does not advance this tick), but never breaks the
    Vehicle contract: position never decreases and move() never raises.
    """

    symbol = "\U0001F699"

    def move(self) -> None:
        if random.random() < 0.3:
            return  # stalled this tick - stays exactly where it is
        self.position += 5


def main():
    vehicles = [SteadyCar("Reliable Rex"), UnreliableCar("Shaky Sam")]
    Track(length=30).run(vehicles)


if __name__ == "__main__":
    main()

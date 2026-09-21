"""
Exercise 1 - Single Responsibility Principle (SRP)

Run this file directly to see the race:
    python -m exercises.ex1_srp
"""
from engine.track import Track


class Car:
    """Holds a car's race state and knows how to move itself. Nothing else."""

    def __init__(self, name: str, speed: int, symbol: str = "\U0001F697"):
        self.name = name
        self.speed = speed
        self.symbol = symbol
        self.position = 0

    def move(self) -> None:
        self.position += self.speed


class RaceLogger:
    """Responsible for recording and persisting race results. Nothing else."""

    def __init__(self):
        self._entries = []

    def record(self, tick, racers) -> None:
        for r in racers:
            self._entries.append(f"tick={tick} {r.name}={r.position}m")

    def save(self, path: str = "race_log.txt") -> None:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(self._entries))

    @property
    def entries(self):
        return list(self._entries)


def main():
    cars = [Car("Red", 4), Car("Blue", 5), Car("Green", 3)]
    logger = RaceLogger()
    track = Track(length=30)
    track.run(cars, on_tick=logger.record)
    logger.save()
    print(f"Saved {len(logger.entries)} log entries to race_log.txt")


if __name__ == "__main__":
    main()

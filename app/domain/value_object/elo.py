from dataclasses import dataclass


@dataclass(frozen=True)
class Elo:
    value: int

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("Elo cannot be negative")

    def increase(self, amount: int) -> "Elo":
        return Elo(self.value + amount)

    def decrease(self, amount: int) -> "Elo":
        return Elo(max(0, self.value - amount))

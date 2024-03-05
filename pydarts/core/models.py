from dataclasses import dataclass, field


@dataclass()
class Game():
    players: list["Player"]


@dataclass()
class Player():
    name: str
    score: int
    history: list[list[int]] = field(default_factory=list)

    def add_turn(self, turn: list[int]) -> None:
        self.score -= sum(turn)
        self.history.append(turn)
        return None

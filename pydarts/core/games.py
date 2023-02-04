from abc import ABC, abstractmethod
from dataclasses import dataclass


class GameIdError(Exception):
    def __init__(self, id: str):
        super().__init__(f"no game available for id: {id!r}")


@dataclass(frozen=True)
class MetadataElement():
    """
    The metadata of a game, e.g. name and description.
    """

    id: str
    display_name: str
    description: str


class Metadata():
    """
    The metadata of all games. Purpose of this class is to provide
    a flexible and scalable interface between GUI and game classes.
    """

    _games: tuple[MetadataElement]

    @classmethod
    def load(cls):
        cls._games = (
            MetadataElement("301", "301", "Wirf exakt 301 Punkte."),
            MetadataElement("501", "501", "Wirf exakt 501 Punkte."),
            MetadataElement(
                "around_the_clock", "Around the Clock",
                "Wirf der Reihe nach von 1 bis Bull's-eye"
            )
        )

    @classmethod
    def get_games(cls) -> tuple[MetadataElement]:
        return cls._games

    @classmethod
    def get_ids(cls) -> list[str]:
        return [game.id for game in cls.get_games()]

    @classmethod
    def get_game(cls, id: str) -> MetadataElement:
        for game in cls.get_games():
            if game.id == id:
                return game
        raise GameIdError(id)


class BaseGame(ABC):
    def __init__(self, metadata: MetadataElement) -> None:
        self.metadata: MetadataElement = metadata

    def __repr__(self) -> str:
        return self.metadata.__repr__()


class Game301(BaseGame):
    def __init__(self) -> None:
        super().__init__(Metadata.get_game("301"))


class Game501(BaseGame):
    def __init__(self) -> None:
        super().__init__(Metadata.get_game("501"))


def build_game_for(id: str) -> BaseGame:
    if id == "301":
        return Game301()
    elif id == "501":
        return Game501()
    else:
        raise GameIdError(id)

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# ---------------------------- BEGIN EXCEPTIONS ----------------------------- #

class GameIdError(Exception):
    def __init__(self, id: str):
        super().__init__(f"no game available for id: {id!r}")

# ----------------------------- END EXCEPTIONS ------------------------------ #


# ########################################################################### #


# ----------------------------- BEGIN METADATA ------------------------------ #

@dataclass(frozen=True)
class _GameMetadata():
    """
    The metadata of a game, e.g. name and description.
    """

    id: str
    display_name: str
    description: str


@dataclass(frozen=True)
class _GamesMetadata():
    """
    The metadata of all games. Purpose of this class is to provide
    a flexible and scalable interface between the GUI and game APIs.
    """

    games: list[_GameMetadata] = field(default_factory=list)

    def get_ids(self):
        return [ game.id for game in self.games ]

    def get_game_for(self, id: str) -> _GameMetadata:
        for game in self.games:
            if game.id == id:
                return game
        raise GameIdError(id)

    def get_display_name_for(self, id: str):
        return self.get_game_for(id).display_name

    def get_description_for(self, id: str):
        return self.get_game_for(id).description


METADATA = _GamesMetadata([
    _GameMetadata("301", "301", "Wirf exakt 301 Punkte."),
    _GameMetadata("501", "501", "Wirf exakt 501 Punkte.")
])

# ------------------------------ END METADATA ------------------------------- #


# ########################################################################### #


# ------------------------------- BEGIN GAME -------------------------------- #

class Game(ABC):
    def __init__(self, metadata: _GameMetadata) -> None:
        self.metadata: _GameMetadata = metadata

    def __repr__(self) -> str:
        return self.metadata.__repr__()


class Game301(Game):
    def __init__(self) -> None:
        super().__init__(METADATA.get_game_for("301"))


class Game501(Game):
    def __init__(self) -> None:
        super().__init__(METADATA.get_game_for("501"))


def build_game_for(id: str) -> Game:
    if id == "301":
        return Game301()
    elif id == "501":
        return Game501()
    else:
        raise GameIdError(id)

# -------------------------------- END GAME --------------------------------- #

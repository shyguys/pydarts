from abc import ABC, abstractmethod

import pydarts.core.errors as errors
import pydarts.core.metadata as metadata


class BaseMode(ABC):
    def __init__(self, metadata: metadata.Mode) -> None:
        self.metadata = metadata

    def __repr__(self) -> str:
        return self.metadata.__repr__()


class Mode301(BaseMode):
    def __init__(self) -> None:
        super().__init__(metadata.Modes.get_mode("301"))


class Mode501(BaseMode):
    def __init__(self) -> None:
        super().__init__(metadata.Modes.get_mode("501"))


def build_game_for(id: str) -> BaseMode:
    if id == "301":
        return Mode301()
    if id == "501":
        return Mode501()
    raise errors.GameIdError(id)

from dataclasses import dataclass

import pydarts.core.errors as errors


_MODES = {
    "301": {
        "name": "301",
        "description": "Throw exactly 301 points."
    },
    "501": {
        "name": "501",
        "description": "Throw exactly 501 points."
    },
    "around_the_clock": {
        "name": "Around the Clock",
        "description": "From 1 to Bull's-eye in order."
    }
}


@dataclass(frozen=True)
class Mode():
    """
    The metadata of a mode, e.g. name and description.
    """

    id: str
    name: str
    description: str


class Modes():
    """
    The metadata of all games. Purpose of this class is to provide
    a flexible and scalable interface between GUI and game classes.
    """

    @classmethod
    def get_ids(self) -> list[str]:
        return [k for k in _MODES]
    
    @classmethod
    def get_mode(self, id: str) -> Mode:
        for k in _MODES:
            if k == id:
                return Mode(k, _MODES[id]["name"], _MODES[id]["description"])
        raise errors.GameIdError(id)

    @classmethod
    def get_modes(cls) -> list[Mode]:
        return [cls.get_mode(id) for id in cls.get_ids()]

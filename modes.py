from abc import ABC, abstractmethod
from dataclasses import dataclass

_MODES_METADATA = {
    "301": {
        "display_name": "301",
        "description": "Wirf exakt 301 Punkte."
    },
    "501": {
        "display_name": "501",
        "description": "Wirf exakt 501 Punkte."
    }
}

def get_ids() -> list[str]:
    return list(_MODES_METADATA.keys())

def get_metadata_fields() -> list[str]:
    return list(_MODES_METADATA[list(_MODES_METADATA.keys())[0]].keys())

def get_metadata_of(id: str) -> dict [str, str]:
    return _MODES_METADATA[id]

def get_display_name_of(id: str) -> str:
    return get_metadata_of(id)["display_name"]

def get_description_of(id: str) -> str:
    return get_metadata_of(id)["description"]


@dataclass(frozen=True)
class ModeMetadata():
    id: str
    display_name: str
    description: str


def build_mode_metadata_of(id: str) -> ModeMetadata:
    return ModeMetadata(id, get_display_name_of(id), get_description_of(id))


class Mode(ABC):
    def __init__(self, metadata: ModeMetadata) -> None:
        self.metadata: ModeMetadata = metadata

    def __repr__(self) -> str:
        return ModeMetadata.__repr__(self.metadata)


class Mode301(Mode):
    def __init__(self) -> None:
        super().__init__(build_mode_metadata_of("301"))


class Mode501(Mode):
    def __init__(self) -> None:
        super().__init__(build_mode_metadata_of("501"))

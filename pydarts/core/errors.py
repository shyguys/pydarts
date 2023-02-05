class GameIdError(Exception):
    def __init__(self, id: str):
        super().__init__(f"no game available for id: {id!r}")

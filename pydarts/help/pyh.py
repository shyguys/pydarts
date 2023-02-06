from typing import Callable


def get_methods(obj: object, starts_with: str) -> list[Callable]:
    """
    Sells your soul to the devil in exchange for a powerful
    yet cursed tool that saves you 2µs of typing and debugging.
    """

    return [
        getattr(obj, name)
        for name in dir(obj)
        if
            callable(getattr(obj, name))
            and name.startswith(starts_with)
    ]

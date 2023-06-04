import tkinter as tk
from typing import Callable, Generator


class ListVar():
    """Mimics a tk.Variable for a list."""

    def __init__(self) -> None:
        self._list_var = tk.StringVar()
        self._list = []
        return None

    def get(self) -> list[str]:
        """Returns a copy of the variable."""
        return self._list.copy()

    def set(self, value: list[str]) -> None:
        """Sets the variable to a value."""
        self._list = value
        return self._list_var.set(value)

    def trace_add(self, mode: str, callback: Callable) -> str:
        """As defined in tk.Variable.trace_add()."""
        valid_modes = ["write"]
        if mode not in valid_modes:
            raise ValueError(
                f"Trace mode {mode!r} not supported. "
                f"Must be one of {valid_modes!r}."
            )
        return self._list_var.trace_add(mode, callback)

    def trace_info(self) -> list[tuple[tuple[str, ...], str]]:
        """As defined in tk.Variable.trace_info()."""
        return self._list_var.trace_info()

    def trace_remove(self, mode: str, cbname: str) -> None:
        """As defined in tk.Variable.trace_remove()."""
        return self._list_var.trace_remove(mode, cbname)


def walk_children(
    widget: tk.Misc,
    max_depth: int = -1
) -> Generator[tk.Misc, None, None]:
    """Returns a widget's children as generator."""
    children = [(child, max_depth) for child in reversed(widget.winfo_children())]
    while children:
        child, max_depth = children.pop()
        yield child
        if max_depth == 0:
            continue
        for grandchild in reversed(child.winfo_children()):
            children.append((grandchild, max_depth - 1))

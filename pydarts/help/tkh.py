import tkinter as tk
from typing import Generator


class ListVar():
    """Mimics a tk.Variable for a list."""

    def __init__(self):
        self._list_var = tk.StringVar()
        self._list = []

    def get(self) -> list[str]:
        """Returns a copy of the variable."""
        return self._list.copy()

    def set(self, value: list[str]):
        """Sets the variable to a value."""
        self._list = value
        self._list_var.set(value)

    def trace_add(self, *args, **kwargs):
        """As defined in tk.Variable.trace_add()."""
        self._list_var.trace_add(*args, **kwargs)

    def trace_info(self):
        """As defined in tk.Variable.trace_info()."""
        self._list_var.trace_info()

    def trace_remove(self, *args, **kwargs):
        """As defined in tk.Variable.trace_remove()."""
        self._list_var.trace_remove(*args, **kwargs)


def walk_children(
    widget: tk.Misc,
    max_depth: int = -1
) -> Generator[tk.Misc, None, None]:
    """Returns a widget's children as generator."""
    children = [
        (child, max_depth) for child in reversed(widget.winfo_children())
    ]
    while children:
        child, max_depth = children.pop()
        yield child
        if max_depth == 0:
            continue
        for grandchild in reversed(child.winfo_children()):
            children.append((grandchild, max_depth-1))

import tkinter as tk
from typing import Generator


def walk_children(widget: tk.Widget, max_depth: int = -1) \
    -> Generator[tk.Widget, None, None]:

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


class ListVar():
    def __init__(self):
        self._list_var = tk.StringVar()
        self._list = []
    
    def get(self) -> list[str]:
        return self._list.copy()
    
    def set(self, players: list[str]):
        self._list = players
        self._list_var.set(players)
    
    def trace_add(self, *args, **kwargs):
        self._list_var.trace_add(*args, **kwargs)

    def trace_info(self):
        self._list_var.trace_info()

    def trace_remove(self, *args, **kwargs):
        self._list_var.trace_remove(*args, **kwargs)

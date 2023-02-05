import tkinter as tk
import tkinter.ttk as ttk
from enum import Enum
from typing import Generator


class CustomEvent(Enum):
    OVERVIEW_TAB_FINISHED = "<<OverviewTabFinished>>"
    PREGAME_WINDOW_FINISHED = "<<PregameWindowFinished>>"


class BaseWidget():
    """
    tbc
    """

    def __init__(self, parent: ttk.Widget):
        self._parent = parent
        self._root = ttk.Frame(master=self._parent)

    @property
    def parent(self) -> ttk.Widget:
        return self._parent

    @property
    def root(self) -> ttk.Frame:
        return self._root


class BaseTab(BaseWidget):
    """
    tbc
    """

    def __init__(self, parent: ttk.Notebook):
        super().__init__(parent)

    @property
    def parent(self) -> ttk.Notebook:
        return super().parent

    def handle_change_to_self(self, event: tk.Event = None):
        ...

    def is_active(self) -> bool:
        return self.parent.index(self.root) == self.parent.index("current")


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

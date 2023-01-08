import tkinter as tk
from typing import Generator

def walk_children(
        widget: tk.Widget, max_depth: int = -1
        ) -> Generator[tk.Widget, None, None]:
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

def is_parent_of(parent: tk.Widget, widget: tk.Widget) -> bool:
    for child in walk_children(parent):
        if child is widget:
            return True
    return False

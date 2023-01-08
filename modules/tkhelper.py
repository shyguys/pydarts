import tkinter as tk
from typing import Generator

def walk_children(widget: tk.Widget) -> Generator[tk.Widget, None, None]:
    children = widget.winfo_children()
    while children:
        child = children.pop()
        yield child
        for grandchild in reversed(child.winfo_children()):
            children.append(grandchild)

def is_parent_of(parent: tk.Widget, widget: tk.Widget) -> bool:
    for child in walk_children(parent):
        if child is widget:
            return True
    return False

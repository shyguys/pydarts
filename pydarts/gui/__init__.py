import tkinter as tk
from enum import StrEnum
from typing import Iterable

import pydarts
import pydarts.gui.pregame


class Stage(StrEnum):
    PREGAME = "pregame"
    GAME = "game"
    POSTGAME = "postgame"


class App(tk.Tk):
    def __init__(self, enable_debug: bool, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.enable_debug = enable_debug
        self.title("PyDarts")
        self.iconbitmap(pydarts.assets_dir / "icon.ico")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.pregame: pydarts.gui.pregame.Root

        self._load_stage(Stage.PREGAME)
        return None

    def _enable_debug(self):
        highlight_children(self)
        sequences = []
        for sequence in sequences:
            self.bind_all(sequence, self._handle_event)

    def _handle_event(self, event: tk.Event):
        pydarts.logger.debug(
            f"application caught event:\n"
            f"  event: {event!r}\n"
            f"  widget: {event.widget!r}"
        )

    def _load_stage(self, stage: Stage) -> None:
        self.resizable(True, True)
        if stage == Stage.PREGAME:
            self.pregame = pydarts.gui.pregame.Root(self)
            width, height = 640, 360
            self.resizable(False, False)
            widget = self.pregame
        widget.grid(column=0, row=0, sticky="NSEW")
        x, y = (self.winfo_screenwidth() - width) // 2, (self.winfo_screenheight() - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")
        if self.enable_debug:
            self._enable_debug()
        return None


def highlight_children(parent: tk.Misc):
    for widget in walk_children(parent):
        try:
            widget.configure(borderwidth=1, relief="solid")  # type: ignore
        except tk.TclError:
            # widget does not support borders, fine
            pass


def walk_children(parent: tk.Misc, max_depth: int = -1) -> Iterable[tk.Misc]:
    children = [(child, max_depth) for child in reversed(parent.winfo_children())]
    while children:
        child, max_depth = children.pop()
        yield child
        if max_depth == 0:
            continue
        for grandchild in reversed(child.winfo_children()):
            children.append((grandchild, max_depth - 1))

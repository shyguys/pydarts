from typing import Optional

from PySide6.QtWidgets import QApplication

import pydarts
from pydarts.core import models
from pydarts.widgets.main_window import MainWindow


class Application(QApplication):
    def __init__(self, args: list[str]) -> None:
        super().__init__(args)
        self.setApplicationName("pydarts")
        self.setApplicationDisplayName("PyDarts")
        self.setApplicationVersion(pydarts.__version__)
        self.main_window: MainWindow
        self._load_main_window()
        return None

    def _load_main_window(self, game: Optional[models.BaseGame] = None) -> None:
        if game is not None:
            self.main_window.destroy()
        self.main_window = MainWindow(game)
        self.main_window.finished_exit.connect(self.quit)
        self.main_window.finished_play_again.connect(lambda game: self._load_main_window(game))
        return None

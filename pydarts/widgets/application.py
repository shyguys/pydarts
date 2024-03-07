from PySide6.QtWidgets import QApplication

import pydarts
from pydarts.core.models import Game
from pydarts.widgets.main_window import MainWindow


class Application(QApplication):
    def __init__(self, args: list[str]) -> None:
        super().__init__(args)
        self.main_window: MainWindow = None  # type: ignore --> see self.load
        self.setApplicationName("pydarts")
        self.setApplicationDisplayName("PyDarts")
        self.setApplicationVersion(pydarts.__version__)
        self.load()
        return None

    def load(self, game: Game | None = None) -> None:
        self.main_window = MainWindow(game=game)
        self.main_window.show()
        self.setup_logic()
        return None

    def setup_logic(self) -> None:
        self.setup_main_window()
        return None

    def setup_main_window(self) -> None:
        self.main_window.finished_exit.connect(self.main_window_finished_exit)
        self.main_window.finished_play_again.connect(self.main_window_finished_play_again)
        return None

    def main_window_finished_exit(self) -> None:
        self.quit()
        return None

    def main_window_finished_play_again(self, game: Game) -> None:
        self.load(game)
        return None

from PySide6.QtWidgets import QApplication

import pydarts
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

    def _load_main_window(self) -> None:
        self.main_window = MainWindow()
        self.main_window.finished_exit.connect(self.quit)
        return None

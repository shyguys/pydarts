import sys

from PySide6.QtWidgets import QApplication, QMainWindow

import pydarts


class Application(QApplication):
    def __init__(self, args: list[str] = sys.argv) -> None:
        super().__init__(args)
        self.setApplicationName("pydarts")
        self.setApplicationDisplayName("PyDarts")
        self.setApplicationVersion(pydarts.__version__)
        return None


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(600, 400)
        return None

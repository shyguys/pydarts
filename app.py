import typing

from PyQt5.QtWidgets import QApplication

class PyDartsApp(QApplication):
    def __init__(self, argv: typing.List[str]):
        super().__init__(argv)

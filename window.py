from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow

class PyDartsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyDarts")
        self.setMinimumSize(QSize(800, 600))

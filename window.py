from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QVBoxLayout, QWidget, QListWidget)


class PyDartsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_appearance()
        self.set_widgets()
        self.players = []

    def set_appearance(self):
        self.setWindowTitle("PyDarts")
        self.setMinimumSize(QSize(800, 600))

    def set_widgets(self):
        root_widget = QWidget()
        self.setCentralWidget(root_widget)

        root_layout = QVBoxLayout()
        root_widget.setLayout(root_layout)

        text_layout = QHBoxLayout()
        text_layout.addWidget(QLabel("Enter player name:"))
        text_layout.addWidget(QLineEdit())
        text_layout.addWidget(QPushButton("add"))
        root_layout.addLayout(text_layout)

        player_overview_widget = QListWidget()

    def add_player(self):
        pass

from PySide6.QtWidgets import QMainWindow, QWidget

from pydarts.core.models import Game
from pydarts.widgets.game_widget import GameWidget
from pydarts.widgets.post_game_widget import PostGameWidget
from pydarts.widgets.pre_game_widget import PreGameWidget
from pydarts.widgets.ui.main_window import Ui_main_window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.pre_game_widget = PreGameWidget(parent=self)
        self.pre_game_widget.hide()
        self.game_widget = GameWidget(parent=self)
        self.game_widget.hide()
        self.post_game_widget = PostGameWidget(parent=self)
        self.post_game_widget.hide()
        self.load_central_widget(self.pre_game_widget)
        self.setup_logic()

    def load_central_widget(self, widget: QWidget) -> None:
        self.centralWidget().hide()
        self.setCentralWidget(widget)
        self.setMinimumSize(widget.minimumSize())
        self.setMaximumSize(widget.maximumSize())
        self.setWindowTitle(widget.windowTitle())
        widget.show()
        return None

    def setup_logic(self) -> None:
        self.setup_pre_game_widget()
        return None

    def setup_pre_game_widget(self) -> None:
        self.pre_game_widget.finished.connect(self.pre_game_widget_finished)

    def pre_game_widget_finished(self, game: Game) -> None:
        self.game_widget.load_game(game)
        self.load_central_widget(self.game_widget)

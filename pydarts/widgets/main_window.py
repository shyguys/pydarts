from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QWidget

from pydarts.core.models import Game
from pydarts.widgets.game_widget import GameWidget
from pydarts.widgets.post_game_widget import PostGameWidget
from pydarts.widgets.pre_game_widget import PreGameWidget
from pydarts.widgets.ui.main_window import Ui_main_window


class MainWindow(QMainWindow):
    finished_play_again = Signal(Game, arguments=["game"])
    finished_exit = Signal()

    def __init__(self, game: Game | None = None):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.pre_game_widget: PreGameWidget = None  # type: ignore --> see self.load
        self.game_widget: GameWidget = None  # type: ignore --> see self.load
        self.post_game_widget: PostGameWidget = None  # type: ignore --> see self.load
        self.load(game)

    def load(self, game: Game | None = None) -> None:
        self.pre_game_widget = PreGameWidget(parent=self, game=game)
        self.pre_game_widget.hide()
        self.game_widget = GameWidget(parent=self)
        self.game_widget.hide()
        self.post_game_widget = PostGameWidget(parent=self)
        self.post_game_widget.hide()
        self.load_central_widget(self.pre_game_widget)
        self.setup_logic()
        return None

    def load_central_widget(self, widget: QWidget) -> None:
        self.hide()
        self.centralWidget().hide()
        self.setCentralWidget(widget)
        self.setMinimumSize(widget.minimumSize())
        self.setMaximumSize(widget.maximumSize())
        self.setGeometry(widget.geometry())
        self.move(self.screen().geometry().center() - self.geometry().center())
        self.setWindowTitle(widget.windowTitle())
        widget.show()
        self.show()
        return None

    def setup_logic(self) -> None:
        self.setup_pre_game_widget()
        self.setup_game_widget()
        self.setup_post_game_widget()
        return None

    def setup_pre_game_widget(self) -> None:
        self.pre_game_widget.finished.connect(self.pre_game_widget_finished)

    def setup_game_widget(self) -> None:
        self.game_widget.finished.connect(self.game_widget_finished)

    def setup_post_game_widget(self) -> None:
        self.post_game_widget.finished_exit.connect(self.post_game_widget_finished_exit)
        self.post_game_widget.finished_play_again.connect(self.post_game_widget_finished_play_again)

    def pre_game_widget_finished(self, game: Game) -> None:
        self.load_central_widget(self.game_widget)
        self.game_widget.load(game)

    def game_widget_finished(self, game: Game) -> None:
        self.load_central_widget(self.post_game_widget)
        self.post_game_widget.load(game)

    def post_game_widget_finished_exit(self) -> None:
        self.finished_exit.emit()
        return None

    def post_game_widget_finished_play_again(self, game: Game) -> None:
        self.finished_play_again.emit(game)

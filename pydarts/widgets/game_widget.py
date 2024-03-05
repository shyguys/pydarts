from PySide6.QtWidgets import QWidget

from pydarts.core.models import Game
from pydarts.widgets.ui.game_widget import Ui_game_widget


class GameWidget(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.ui = Ui_game_widget()
        self.ui.setupUi(self)
        self.game: Game = None  # type: ignore --> see self.load_game
        self.setup_logic()

    def setup_logic(self) -> None:
        return None

    def load_game(self, game: Game) -> None:
        self.game = game
        return None

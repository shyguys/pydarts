from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from pydarts.core.models import Game
from pydarts.widgets.ui.post_game_widget import Ui_post_game_widget


class PostGameWidget(QWidget):
    finished_play_again = Signal(Game, arguments=["game"])
    finished_exit = Signal()

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.ui = Ui_post_game_widget()
        self.game: Game = None  # type: ignore --> see self.load
        self.ui.setupUi(self)
        self.load()

    def load(self, game: Game | None = None) -> None:
        self.setup_logic()
        if game is None:
            return None
        self.game = game
        self.ui.leaderboard_value_label.setText("\n".join(
            f"{index+1}. {player.name} ({player.score})"
            for index, player in
            enumerate(sorted(self.game.players, key=lambda p: p.score))
        ))
        return None

    def setup_logic(self) -> None:
        self.setup_exit_game_push_button()
        self.setup_play_again_push_button()
        return None

    def setup_exit_game_push_button(self) -> None:
        self.ui.exit_game_push_button.released.connect(self.exit_game_push_button_released)
        return None

    def setup_play_again_push_button(self) -> None:
        self.ui.play_again_push_button.released.connect(self.play_again_push_button_released)
        return None

    def exit_game_push_button_released(self) -> None:
        self.finished_exit.emit()
        return None

    def play_again_push_button_released(self) -> None:
        self.finished_play_again.emit(self.game)
        return None

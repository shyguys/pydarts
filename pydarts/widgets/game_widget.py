from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit, QWidget

from pydarts.core.models import Game
from pydarts.widgets.ui.game_widget import Ui_game_widget


class GameWidget(QWidget):
    finished = Signal(Game, arguments=["game"])

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.ui = Ui_game_widget()
        self.game: Game = None  # type: ignore --> see self.load
        self.ui.setupUi(self)
        self.load()

    def load(self, game: Game | None = None) -> None:
        if game is None:
            return None
        self.game = game
        self.ui.turn_order_value_label.setText("\n".join(p.name for p in game.players))
        self.activate_player(0)
        self.setup_logic()
        return None

    def setup_logic(self) -> None:
        self.setup_register_push_button()
        self.setup_finish_game_push_button()
        return None

    def setup_register_push_button(self) -> None:
        self.ui.register_push_button.released.connect(self.register_push_button_released)
        return None

    def setup_finish_game_push_button(self) -> None:
        self.ui.finish_game_push_button.released.connect(self.finish_game_push_button_released)
        return None

    def register_push_button_released(self) -> None:
        turn: list[int] = []
        for child in self.ui.throws_widget.children():
            if not isinstance(child, QLineEdit):
                continue
            throw = int(value) if (value := child.text().strip()) else 0
            turn.append(throw)
            child.setText("")
        player_name = self.ui.current_player_value_label.text()
        for i, p in enumerate(self.game.players):
            if p.name == player_name:
                index, player = i, p
        player.add_turn(turn)
        index = 0 if (index == len(self.game.players) - 1) else index + 1
        self.activate_player(index)
        return None

    def finish_game_push_button_released(self) -> None:
        self.finished.emit(self.game)
        return None

    def activate_player(self, index: int) -> None:
        player = self.game.players[index]
        self.ui.current_player_value_label.setText(player.name)
        self.ui.score_value_label.setText(str(player.score))
        return None

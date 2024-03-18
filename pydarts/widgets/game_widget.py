from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from pydarts.core import models
from pydarts.widgets.ui.game_widget import Ui_game_widget


class GameWidget(QWidget, Ui_game_widget):
    finished = Signal(models.BaseGame, arguments=["game"])

    def __init__(self, parent: QWidget, game: models.BaseGame) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._load_event_handling()
        self.game = game
        self._activate_next_player()
        return None

    def _load_event_handling(self) -> None:
        self.throw_input_line_edit.returnPressed.connect(self._register_throw)
        self.next_turn_push_button.released.connect(self._continue_to_next_turn)
        self.finish_game_push_button.released.connect(self._end_game)
        return None

    def _draw(self) -> None:
        current_player = self.game.get_active_player()
        self.turn_order_value_label.setText("\n".join(
            f"{index+1}. {player.name} ({player.score})"
            for index, player in enumerate(self.game.players)
        ))
        index = self.game.players.index(current_player)
        self.current_player_value_label.setText(f"{current_player.name} ({current_player.score})")
        for index, line_edit in enumerate([self.throw_1_line_edit, self.throw_2_line_edit, self.throw_3_line_edit]):
            try:
                throw = current_player.history[-1][index]
            except IndexError:
                line_edit.setText("")
            else:
                line_edit.setText(throw.value)
        self.throw_input_line_edit.setText("")
        if self.game.is_over or current_player.is_turn_over:
            self.throw_input_line_edit.setDisabled(True)
        else:
            self.throw_input_line_edit.setEnabled(True)
        return None

    def _activate_next_player(self) -> None:
        self.game.activate_next_player()
        self._draw()
        return None

    def _register_throw(self) -> None:
        try:
            throw = models.Throw(self.throw_input_line_edit.text().strip().upper())
        except ValueError:
            self.throw_input_line_edit.setText("")
            return None
        try:
            self.game.register_throw(throw)
        except models.ValueLimitExceededError:
            self.hint_label.setText("Too much! Try again next round.\n\nPress 'Next' to activate next player.")
            self._draw()
            return None
        if self.game.is_over:
            self.hint_label.setText("You won, congratulations!\n\nPress 'Finish' to end game.")
        elif self.game.get_active_player().is_turn_over:
            self.hint_label.setText("Press 'Next' to activate next player.")
        self._draw()
        return None

    def _continue_to_next_turn(self) -> None:
        self.hint_label.setText("")
        current_player = self.game.get_active_player()
        current_turn = current_player.history[-1]
        for _ in range(len(current_turn), 3):
            current_turn.append(models.Throw("0"))
        self._activate_next_player()
        return None

    def _end_game(self) -> None:
        self.finished.emit(self.game)
        return None

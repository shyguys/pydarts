from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget

from pydarts.core.models import Game, Player
from pydarts.widgets.ui.pre_game_widget import Ui_pre_game_widget


class PreGameWidget(QWidget):
    finished = Signal(Game, arguments=["game"])

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.ui = Ui_pre_game_widget()
        self.ui.setupUi(self)
        self.setup_logic()

    def setup_logic(self) -> None:
        self.setup_input_line_edit()
        self.setup_add_push_button()
        self.setup_remove_push_button()
        self.setup_move_up_push_button()
        self.setup_move_down_push_button()
        self.setup_start_game_push_button()
        return None

    def setup_input_line_edit(self) -> None:
        self.ui.input_line_edit.returnPressed.connect(self.input_line_edit_returnPressed)
        return None

    def setup_add_push_button(self) -> None:
        self.ui.add_push_button.released.connect(self.add_push_button_released)
        return None

    def setup_remove_push_button(self) -> None:
        self.ui.remove_push_button.released.connect(self.remove_push_button_released)
        return None

    def setup_move_up_push_button(self) -> None:
        self.ui.move_up_push_button.released.connect(self.move_up_push_button_released)
        return None

    def setup_move_down_push_button(self) -> None:
        self.ui.move_down_push_button.released.connect(self.move_down_push_button_released)
        return None

    def setup_start_game_push_button(self) -> None:
        self.ui.start_game_push_button.released.connect(self.start_game_push_button_released)
        return None

    def input_line_edit_returnPressed(self) -> None:
        self.ui.add_push_button.released.emit()
        return None

    def add_push_button_released(self) -> None:
        new_player_name = self.ui.input_line_edit.text().strip()
        if (
            new_player_name and
            not self.ui.overview_list_widget.findItems(new_player_name, Qt.MatchFlag.MatchFixedString)
        ):
            self.ui.overview_list_widget.addItem(new_player_name)
        self.ui.input_line_edit.setText("")
        return None

    def remove_push_button_released(self) -> None:
        current_row = self.ui.overview_list_widget.currentRow()
        if current_row == -1:
            return None
        self.ui.overview_list_widget.takeItem(current_row)
        return None

    def move_up_push_button_released(self) -> None:
        current_row = self.ui.overview_list_widget.currentRow()
        if current_row < 1:
            return None
        current_player = self.ui.overview_list_widget.takeItem(current_row)
        new_index = current_row-1
        self.ui.overview_list_widget.insertItem(new_index, current_player)
        self.ui.overview_list_widget.setCurrentRow(new_index)
        return None

    def move_down_push_button_released(self) -> None:
        current_row = self.ui.overview_list_widget.currentRow()
        if current_row == -1 or current_row == self.ui.overview_list_widget.count() - 1:
            return None
        current_player = self.ui.overview_list_widget.takeItem(current_row)
        new_index = current_row+1
        self.ui.overview_list_widget.insertItem(new_index, current_player)
        self.ui.overview_list_widget.setCurrentRow(new_index)
        return None

    def start_game_push_button_released(self) -> None:
        players = [
            Player(item.text(), 301) for item in
            self.ui.overview_list_widget.findItems(".+", Qt.MatchFlag.MatchRegularExpression)
        ]
        game = Game(players)
        self.finished.emit(game)
        return None

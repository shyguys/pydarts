from PySide6.QtWidgets import QWidget

from pydarts.widgets.ui.post_game_widget import Ui_post_game_widget


class PostGameWidget(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self.ui = Ui_post_game_widget()
        self.ui.setupUi(self)
        self.setup_logic()

    def setup_logic(self) -> None:
        return None

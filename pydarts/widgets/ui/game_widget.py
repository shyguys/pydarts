# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_game_widget(object):
    def setupUi(self, game_widget):
        if not game_widget.objectName():
            game_widget.setObjectName(u"game_widget")
        game_widget.resize(1600, 900)
        game_widget.setMinimumSize(QSize(1600, 900))
        game_widget.setMaximumSize(QSize(1600, 900))
        self.verticalLayout = QVBoxLayout(game_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_widget = QWidget(game_widget)
        self.input_widget.setObjectName(u"input_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.input_widget.sizePolicy().hasHeightForWidth())
        self.input_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.input_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.darts_widget = QWidget(self.input_widget)
        self.darts_widget.setObjectName(u"darts_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.darts_widget.sizePolicy().hasHeightForWidth())
        self.darts_widget.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.darts_widget)

        self.turn_widget = QWidget(self.input_widget)
        self.turn_widget.setObjectName(u"turn_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.turn_widget.sizePolicy().hasHeightForWidth())
        self.turn_widget.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.turn_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.turn_order_widget = QWidget(self.turn_widget)
        self.turn_order_widget.setObjectName(u"turn_order_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(4)
        sizePolicy3.setHeightForWidth(self.turn_order_widget.sizePolicy().hasHeightForWidth())
        self.turn_order_widget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_7 = QHBoxLayout(self.turn_order_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.turn_order_key_label = QLabel(self.turn_order_widget)
        self.turn_order_key_label.setObjectName(u"turn_order_key_label")
        self.turn_order_key_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.turn_order_key_label)

        self.turn_order_value_label = QLabel(self.turn_order_widget)
        self.turn_order_value_label.setObjectName(u"turn_order_value_label")
        self.turn_order_value_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.turn_order_value_label)


        self.verticalLayout_3.addWidget(self.turn_order_widget)

        self.current_player_widget = QWidget(self.turn_widget)
        self.current_player_widget.setObjectName(u"current_player_widget")
        self.current_player_widget.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.current_player_widget.sizePolicy().hasHeightForWidth())
        self.current_player_widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_2 = QHBoxLayout(self.current_player_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.current_player_key_label = QLabel(self.current_player_widget)
        self.current_player_key_label.setObjectName(u"current_player_key_label")
        sizePolicy2.setHeightForWidth(self.current_player_key_label.sizePolicy().hasHeightForWidth())
        self.current_player_key_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.current_player_key_label)

        self.current_player_value_label = QLabel(self.current_player_widget)
        self.current_player_value_label.setObjectName(u"current_player_value_label")
        sizePolicy2.setHeightForWidth(self.current_player_value_label.sizePolicy().hasHeightForWidth())
        self.current_player_value_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.current_player_value_label)


        self.verticalLayout_3.addWidget(self.current_player_widget)

        self.score_widget = QWidget(self.turn_widget)
        self.score_widget.setObjectName(u"score_widget")
        sizePolicy4.setHeightForWidth(self.score_widget.sizePolicy().hasHeightForWidth())
        self.score_widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_3 = QHBoxLayout(self.score_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.score_key_label = QLabel(self.score_widget)
        self.score_key_label.setObjectName(u"score_key_label")
        sizePolicy2.setHeightForWidth(self.score_key_label.sizePolicy().hasHeightForWidth())
        self.score_key_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.score_key_label)

        self.score_value_label = QLabel(self.score_widget)
        self.score_value_label.setObjectName(u"score_value_label")
        sizePolicy2.setHeightForWidth(self.score_value_label.sizePolicy().hasHeightForWidth())
        self.score_value_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.score_value_label)


        self.verticalLayout_3.addWidget(self.score_widget)

        self.throws_widget = QWidget(self.turn_widget)
        self.throws_widget.setObjectName(u"throws_widget")
        sizePolicy4.setHeightForWidth(self.throws_widget.sizePolicy().hasHeightForWidth())
        self.throws_widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_4 = QHBoxLayout(self.throws_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.throw_1_line_edit = QLineEdit(self.throws_widget)
        self.throw_1_line_edit.setObjectName(u"throw_1_line_edit")

        self.horizontalLayout_4.addWidget(self.throw_1_line_edit)

        self.throw_2_line_edit = QLineEdit(self.throws_widget)
        self.throw_2_line_edit.setObjectName(u"throw_2_line_edit")

        self.horizontalLayout_4.addWidget(self.throw_2_line_edit)

        self.throw_3_line_edit = QLineEdit(self.throws_widget)
        self.throw_3_line_edit.setObjectName(u"throw_3_line_edit")

        self.horizontalLayout_4.addWidget(self.throw_3_line_edit)


        self.verticalLayout_3.addWidget(self.throws_widget)

        self.register_widget = QWidget(self.turn_widget)
        self.register_widget.setObjectName(u"register_widget")
        sizePolicy4.setHeightForWidth(self.register_widget.sizePolicy().hasHeightForWidth())
        self.register_widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_5 = QHBoxLayout(self.register_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.register_push_button = QPushButton(self.register_widget)
        self.register_push_button.setObjectName(u"register_push_button")

        self.horizontalLayout_5.addWidget(self.register_push_button)


        self.verticalLayout_3.addWidget(self.register_widget)

        self.hint_widget = QWidget(self.turn_widget)
        self.hint_widget.setObjectName(u"hint_widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(8)
        sizePolicy5.setHeightForWidth(self.hint_widget.sizePolicy().hasHeightForWidth())
        self.hint_widget.setSizePolicy(sizePolicy5)
        self.horizontalLayout_6 = QHBoxLayout(self.hint_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.hint_label = QLabel(self.hint_widget)
        self.hint_label.setObjectName(u"hint_label")
        self.hint_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_6.addWidget(self.hint_label)


        self.verticalLayout_3.addWidget(self.hint_widget)


        self.horizontalLayout.addWidget(self.turn_widget)


        self.verticalLayout.addWidget(self.input_widget)

        self.finish_game_widget = QWidget(game_widget)
        self.finish_game_widget.setObjectName(u"finish_game_widget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.finish_game_widget.sizePolicy().hasHeightForWidth())
        self.finish_game_widget.setSizePolicy(sizePolicy6)
        self.verticalLayout_2 = QVBoxLayout(self.finish_game_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.finish_game_push_button = QPushButton(self.finish_game_widget)
        self.finish_game_push_button.setObjectName(u"finish_game_push_button")

        self.verticalLayout_2.addWidget(self.finish_game_push_button)


        self.verticalLayout.addWidget(self.finish_game_widget)


        self.retranslateUi(game_widget)

        QMetaObject.connectSlotsByName(game_widget)
    # setupUi

    def retranslateUi(self, game_widget):
        game_widget.setWindowTitle(QCoreApplication.translate("game_widget", u"Game", None))
        self.turn_order_key_label.setText(QCoreApplication.translate("game_widget", u"Turn order:", None))
        self.turn_order_value_label.setText("")
        self.current_player_key_label.setText(QCoreApplication.translate("game_widget", u"Current player:", None))
        self.current_player_value_label.setText("")
        self.score_key_label.setText(QCoreApplication.translate("game_widget", u"Score:", None))
        self.score_value_label.setText("")
        self.register_push_button.setText(QCoreApplication.translate("game_widget", u"Register", None))
        self.hint_label.setText("")
        self.finish_game_push_button.setText(QCoreApplication.translate("game_widget", u"Finish", None))
    # retranslateUi


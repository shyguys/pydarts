# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pre_game_widget.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_pre_game_widget(object):
    def setupUi(self, pre_game_widget):
        if not pre_game_widget.objectName():
            pre_game_widget.setObjectName(u"pre_game_widget")
        pre_game_widget.resize(300, 350)
        pre_game_widget.setMinimumSize(QSize(300, 350))
        pre_game_widget.setMaximumSize(QSize(300, 350))
        pre_game_widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(pre_game_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.player_input_widget = QWidget(pre_game_widget)
        self.player_input_widget.setObjectName(u"player_input_widget")
        self.player_input_widget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.player_input_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.input_label = QLabel(self.player_input_widget)
        self.input_label.setObjectName(u"input_label")

        self.horizontalLayout_3.addWidget(self.input_label)

        self.input_line_edit = QLineEdit(self.player_input_widget)
        self.input_line_edit.setObjectName(u"input_line_edit")

        self.horizontalLayout_3.addWidget(self.input_line_edit)

        self.add_push_button = QPushButton(self.player_input_widget)
        self.add_push_button.setObjectName(u"add_push_button")

        self.horizontalLayout_3.addWidget(self.add_push_button)


        self.verticalLayout.addWidget(self.player_input_widget)

        self.player_overview_widget = QWidget(pre_game_widget)
        self.player_overview_widget.setObjectName(u"player_overview_widget")
        self.verticalLayout_2 = QVBoxLayout(self.player_overview_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.overview_list_widget = QListWidget(self.player_overview_widget)
        self.overview_list_widget.setObjectName(u"overview_list_widget")

        self.verticalLayout_2.addWidget(self.overview_list_widget)


        self.verticalLayout.addWidget(self.player_overview_widget)

        self.player_edit_widget = QWidget(pre_game_widget)
        self.player_edit_widget.setObjectName(u"player_edit_widget")
        self.horizontalLayout = QHBoxLayout(self.player_edit_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.remove_push_button = QPushButton(self.player_edit_widget)
        self.remove_push_button.setObjectName(u"remove_push_button")

        self.horizontalLayout.addWidget(self.remove_push_button)

        self.move_up_push_button = QPushButton(self.player_edit_widget)
        self.move_up_push_button.setObjectName(u"move_up_push_button")

        self.horizontalLayout.addWidget(self.move_up_push_button)

        self.move_down_push_button = QPushButton(self.player_edit_widget)
        self.move_down_push_button.setObjectName(u"move_down_push_button")

        self.horizontalLayout.addWidget(self.move_down_push_button)


        self.verticalLayout.addWidget(self.player_edit_widget)

        self.setup_widget = QWidget(pre_game_widget)
        self.setup_widget.setObjectName(u"setup_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.setup_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.start_game_push_button = QPushButton(self.setup_widget)
        self.start_game_push_button.setObjectName(u"start_game_push_button")

        self.horizontalLayout_2.addWidget(self.start_game_push_button)


        self.verticalLayout.addWidget(self.setup_widget)


        self.retranslateUi(pre_game_widget)

        QMetaObject.connectSlotsByName(pre_game_widget)
    # setupUi

    def retranslateUi(self, pre_game_widget):
        pre_game_widget.setWindowTitle(QCoreApplication.translate("pre_game_widget", u"Setup", None))
        self.input_label.setText(QCoreApplication.translate("pre_game_widget", u"Player name:", None))
        self.add_push_button.setText(QCoreApplication.translate("pre_game_widget", u"Add", None))
        self.remove_push_button.setText(QCoreApplication.translate("pre_game_widget", u"Remove", None))
        self.move_up_push_button.setText(QCoreApplication.translate("pre_game_widget", u"Move up", None))
        self.move_down_push_button.setText(QCoreApplication.translate("pre_game_widget", u"Move down", None))
        self.start_game_push_button.setText(QCoreApplication.translate("pre_game_widget", u"Start", None))
    # retranslateUi


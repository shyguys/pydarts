# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'post_game_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_post_game_widget(object):
    def setupUi(self, post_game_widget):
        if not post_game_widget.objectName():
            post_game_widget.setObjectName(u"post_game_widget")
        post_game_widget.resize(300, 350)
        post_game_widget.setMinimumSize(QSize(300, 350))
        post_game_widget.setMaximumSize(QSize(300, 350))
        self.verticalLayout = QVBoxLayout(post_game_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leaderboard_key_label = QLabel(post_game_widget)
        self.leaderboard_key_label.setObjectName(u"leaderboard_key_label")
        self.leaderboard_key_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.leaderboard_key_label)

        self.leaderboard_value_label = QLabel(post_game_widget)
        self.leaderboard_value_label.setObjectName(u"leaderboard_value_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.leaderboard_value_label.sizePolicy().hasHeightForWidth())
        self.leaderboard_value_label.setSizePolicy(sizePolicy)
        self.leaderboard_value_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.leaderboard_value_label)

        self.play_again_push_button = QPushButton(post_game_widget)
        self.play_again_push_button.setObjectName(u"play_again_push_button")

        self.verticalLayout.addWidget(self.play_again_push_button)

        self.exit_game_push_button = QPushButton(post_game_widget)
        self.exit_game_push_button.setObjectName(u"exit_game_push_button")

        self.verticalLayout.addWidget(self.exit_game_push_button)


        self.retranslateUi(post_game_widget)

        QMetaObject.connectSlotsByName(post_game_widget)
    # setupUi

    def retranslateUi(self, post_game_widget):
        post_game_widget.setWindowTitle(QCoreApplication.translate("post_game_widget", u"Results", None))
        self.leaderboard_key_label.setText(QCoreApplication.translate("post_game_widget", u"Leaderboard:", None))
        self.leaderboard_value_label.setText("")
        self.play_again_push_button.setText(QCoreApplication.translate("post_game_widget", u"Play again", None))
        self.exit_game_push_button.setText(QCoreApplication.translate("post_game_widget", u"Exit", None))
    # retranslateUi


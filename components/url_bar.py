from PyQt5.QtWidgets import QComboBox, QTextEdit, QPushButton, QSizePolicy
from PyQt5 import QtCore, QtGui

from helpers import style

from .section import Section


class UrlBar(Section):

    def __init__(self):
        super(UrlBar, self).__init__(layout_type="horizontal")
        self.setObjectName("urlBar")
        self.setStyleSheet(style.url_bar)
        self.set_spacing(0)
        self.dropdown_menu = QComboBox()
        self.dropdown_menu.addItems(["GET", "POST", "PUT", "DELETE"])
        self.dropdown_menu.setStyleSheet(style.type_dropdown)

        self.url_textbox = QTextEdit()
        self.url_textbox.setStyleSheet(style.url_entry)

        self.send_button = QPushButton("SEND")
        self.send_button.setStyleSheet(style.send_button)
        self.send_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setMaximumWidth(600)
        self.add_widget(
            self.dropdown_menu,
            v_policy=QSizePolicy.Expanding,
            h_policy=QSizePolicy.Expanding,
            v_stretch=1,
            h_stretch=1,
        )
        self.add_widget(
            self.url_textbox,
            v_policy=QSizePolicy.Expanding,
            h_policy=QSizePolicy.Expanding,
            v_stretch=1,
            h_stretch=4,
        )
        self.add_widget(
            self.send_button,
            v_policy=QSizePolicy.Expanding,
            h_policy=QSizePolicy.Expanding,
            v_stretch=1,
            h_stretch=1,
        )

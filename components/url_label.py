from PyQt5 import QtCore, QtGui

from PyQt5.QtWidgets import QLabel, QSizePolicy

from .section import Section
from helpers import style


REQUEST_COLOR = {
    "GET": ("blue", "#eeeeff"),
    "DELETE": ("red", "#ffeeee"),
    "POST": ("green", "#eeffee"),
    "PUT": ("#cccc00", "#ffffee"),
}


class UrlLabel(Section):
    clicked = QtCore.pyqtSignal()

    def __init__(self, request_type, request_url):
        super(UrlLabel, self).__init__(layout_type="horizontal")
        self.request_type = request_type
        self.type_label = QLabel(request_type)
        self.text_label = QLabel(request_url)

        self.setStyleSheet(style.url_label)
        self.setMaximumHeight(30)
        self.set_spacing(0)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self._make_url_label()

    def _make_url_label(self):
        self.type_label.setStyleSheet(style.url_type(REQUEST_COLOR[self.request_type]))
        self.type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.text_label.setStyleSheet(style.url_text)
        self.add_widget(
            self.type_label,
            v_policy=QSizePolicy.Expanding,
            h_policy=QSizePolicy.Expanding,
            v_stretch=1,
            h_stretch=1,
        )
        self.add_widget(
            self.text_label,
            v_policy=QSizePolicy.Expanding,
            h_policy=QSizePolicy.Expanding,
            v_stretch=1,
            h_stretch=5
        )

    def mousePressEvent(self, event):
        self.clicked.emit()
        Section.mousePressEvent(self, event)

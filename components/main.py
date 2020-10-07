from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from helpers import style

from .section import Section
from .url_label import UrlLabel


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Yapi")
        self.setMinimumSize(1200, 800)
        self.setStyleSheet(style.main_window)
        self.init_ui()

    def init_ui(self):
        h_box = QHBoxLayout()
        h_box.setContentsMargins(0, 0, 0, 0)
        h_box.setSpacing(1)
        self.setLayout(h_box)

        left_section = Section(layout_type="vertical")
        right_section = Section(layout_type="vertical", h_stretch=3)
        self.generate_left_content(left_section)

        splitter = self.make_main_splitter(left_section, right_section)

        h_box.addWidget(splitter)
        left_section.setStyleSheet(style.main_section)
        right_section.setStyleSheet(style.main_section)

        self.showMaximized()

    @staticmethod
    def generate_left_content(section):
        section.set_spacing(0)
        title_label = QtWidgets.QLabel("Recent Requests")
        title_label.setMinimumWidth(400)
        title_label.setStyleSheet(style.title_label)
        title_label.setMaximumHeight(45)
        section.add_widget(title_label)

        # Test UrlLabel-s later to be replaced with data read from file
        url = UrlLabel("GET", "https://0.0.0.0:80")
        section.add_widget(url)
        url1 = UrlLabel("POST", "https://0.0.0.0:80")
        section.add_widget(url1)
        url1 = UrlLabel("DELETE", "https://0.0.0.0:80")
        section.add_widget(url1)
        url1 = UrlLabel("PUT", "https://0.0.0.0:80")
        section.add_widget(url1)

    @staticmethod
    def make_main_splitter(left, right):
        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(left)
        splitter.addWidget(right)
        splitter.setCollapsible(splitter.indexOf(left), False)
        splitter.setCollapsible(splitter.indexOf(right), False)
        splitter.setStretchFactor(1, 3)
        splitter.setSizes([1, 2000])
        return splitter

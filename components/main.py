from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QScrollArea, QSizePolicy

from helpers import style

from .section import Section
from .url_label import UrlLabel
from .url_bar import UrlBar


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
        left_section.setObjectName("leftSide")
        right_section = Section(layout_type="vertical", h_stretch=3)
        left_section.setMinimumWidth(400)

        right_section.setMinimumWidth(800)
        self.generate_left_content(left_section)
        self.generate_right_content(right_section)

        splitter = self.make_main_splitter(left_section, right_section)

        h_box.addWidget(splitter)
        left_section.setStyleSheet(style.main_section)
        right_section.setStyleSheet(style.main_section)

        self.showMaximized()

    def on_url_label_click(self):
        url_label = self.sender()
        req_type = url_label.type_label.text()
        text = url_label.text_label.text()
        url_bar = self.findChild(UrlBar, "urlBar")
        type_index = url_bar.dropdown_menu.findText(req_type, QtCore.Qt.MatchFixedString)
        if type_index >= 0:
            url_bar.dropdown_menu.setCurrentIndex(type_index)
        url_bar.url_textbox.setText(text)

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

    def generate_left_content(self, section):
        section.set_spacing(0)
        title_label = QtWidgets.QLabel("Recent Requests")
        title_label.setStyleSheet(style.title_label)
        title_label.setFixedHeight(45)
        section.add_widget(title_label)

        urls = self.load_urls_file()
        for url in urls:
            if len(url) == 2:
                url = UrlLabel(url[0], url[1])
                url.clicked.connect(self.on_url_label_click)
                section.add_widget(url)

    def generate_right_content(self, section):
        section.set_spacing(0)
        url_bar_section = UrlBar()
        url_bar_section.send_button.clicked.connect(self.on_send_request)
        url_bar_section.setMaximumHeight(60)
        section.add_widget(url_bar_section)

    @staticmethod
    def load_urls_file():
        file = open("./recent_requests.txt", "r")
        urls = file.read().split("\n")
        return [url.split("-") for url in urls]

    def on_send_request(self):
        url_bar = self.findChild(UrlBar, "urlBar")
        type_request = url_bar.dropdown_menu.currentText()
        url_request = url_bar.url_textbox.toPlainText()
        print((not type_request))
        print((not url_request))
        if not url_request:
            return

        file = open("./recent_requests.txt", "r")
        all_requests = file.read().split("\n")
        if len(all_requests) > 30:
            all_requests = all_requests[:-1]
        updated_requests = [f"{type_request}-{url_request}", *all_requests]

        left = self.findChild(Section, "leftSide")
        print(left.count())
        if left.count() >= 29:
            left.pop()
        new_recent = UrlLabel(type_request, url_request)
        new_recent.clicked.connect(self.on_url_label_click)
        left.insert_widget(1, new_recent)

        self.save_to_file(updated_requests)

    @staticmethod
    def save_to_file(all_requests):
        file = open("./recent_requests.txt", "w")
        file.write("\n".join(all_requests))
        file.close()

import requests
import json

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QScrollArea, QSizePolicy, QPushButton

from PyQt5.QtCore import Qt
from helpers import style

from .section import Section
from .url_label import UrlLabel
from .url_bar import UrlBar
from .result import Result
from .params import Params

REQUEST_TYPE = {
    "GET": requests.get,
    "POST": requests.post,
    "PUT": requests.put,
    "DELETE": requests.delete,
}


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
       
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setMinimumWidth(400)
        scroll.setWidget(left_section)

        splitter = self.make_main_splitter(scroll, right_section)

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

        params = Params()
        params.setFixedHeight(150)
        params.setObjectName("paramsBox")
        section.add_widget(params)

        result = Result()
        result.setFixedHeight(500)
        result.setObjectName("resultBox")
        section.add_widget(result)

        save_button = QPushButton("SAVE")
        save_button.setStyleSheet(style.save_button)
        save_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        save_button.clicked.connect(self.on_save_response)
        save_button.setMaximumHeight(40)
        save_button.setMaximumWidth(200)
        section.add_widget(
            save_button
        )
    @staticmethod
    def load_urls_file():
        file = open("./recent_requests.txt", "r")
        urls = file.read().split("\n")
        return [url.split("-") for url in urls]

    def on_send_request(self):
        url_bar = self.findChild(UrlBar, "urlBar")
        type_request = url_bar.dropdown_menu.currentText()
        url_request = url_bar.url_textbox.toPlainText()
        if not url_request:
            return

        file = open("./recent_requests.txt", "r")
        all_requests = file.read().split("\n")
        if len(all_requests) > 45:
            all_requests = all_requests[:-1]
        updated_requests = [f"{type_request}-{url_request}", *all_requests]

        left = self.findChild(Section, "leftSide")
        if left.count() >= 29:
            left.pop()
        new_recent = UrlLabel(type_request, url_request)
        new_recent.clicked.connect(self.on_url_label_click)
        left.insert_widget(1, new_recent)

        try:

            print(type_request)
            request = REQUEST_TYPE[type_request]
            param_text = self.findChild(Params, "paramsBox").toPlainText()
            params = {}
            try:
                params = json.loads(param_text)
            except Exception as e:
                pass

            if type_request != "GET":
                resp = request(url_request, json=params)
            else:
                resp = request(url_request)
        except Exception as e:
            resp = "Url not found"
        result = self.findChild(Result, "resultBox")
        result.insert_data(resp)
        self.save_to_file(updated_requests)

    def on_save_response(self):
        url_bar = self.findChild(UrlBar, "urlBar")
        try:
            page = url_bar.url_textbox.toPlainText().split("/")[2]
        except Exception as e:
            return
        result = self.findChild(Result, "resultBox")
        response = result.toPlainText()
        try:
            f = open(f"{page}.txt", "a")
            f.write(response)
            f.close()
        except Exception as e:
            pass


    @staticmethod
    def save_to_file(all_requests):
        file = open("./recent_requests.txt", "w")
        file.write("\n".join(all_requests))
        file.close()

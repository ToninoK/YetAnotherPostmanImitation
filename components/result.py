import json

from PyQt5.QtWidgets import QTextEdit

from .section import Section
from helpers import style

class Result(Section):
    def __init__(self):
        super(Result, self).__init__(layout_type="horizontal")
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.setStyleSheet(style.result)
        self.text_edit.setStyleSheet(style.result_text_edit)
        self.text_edit.setPlaceholderText("Response goes here.")
        self.add_widget(self.text_edit)

    def _insert_json(self, data):
        self.text_edit.setPlainText(data)

    def _insert_html(self, data):
        self.text_edit.setHtml(data)

    def insert_data(self, data):
        if type(data) == str:
            self._insert_json(data)
            return
        try:
            json_data = data.json()
            json_data = json.dumps(json_data, indent=4, sort_keys=True)
            self._insert_json(json_data)
        except Exception as e:
            html_data = data.text
            self._insert_html(html_data)

    def toPlainText(self):
        return self.text_edit.toPlainText()
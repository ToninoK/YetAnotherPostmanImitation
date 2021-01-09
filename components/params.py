from PyQt5.QtWidgets import QTextEdit

from .section import Section
from helpers import style

class Params(Section):
    def __init__(self):
        super(Params, self).__init__(layout_type="horizontal")
        self.text_edit = QTextEdit()
        self.setStyleSheet(style.params)
        self.text_edit.setStyleSheet(style.params_text_edit)
        self.text_edit.setPlaceholderText('Params here. Format: {"key": value, "key": value, ...}')
        self.add_widget(self.text_edit)
    
    def toPlainText(self):
        return self.text_edit.toPlainText()
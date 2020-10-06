from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Yapi")
        self.init_ui()

    def init_ui(self):
        h_box = QtWidgets.QHBoxLayout()
        self.setLayout(h_box)
        self.showMaximized()

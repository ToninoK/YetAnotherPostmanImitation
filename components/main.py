from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Yapi")
        self.showMaximized()

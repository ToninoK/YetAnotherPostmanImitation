import sys

from PyQt5.QtWidgets import QApplication

from components.main import Window

app = QApplication([])
app.setStyle('Fusion')


def run():
    window = Window()
    window.show()
    sys.exit(app.exec_())


run()

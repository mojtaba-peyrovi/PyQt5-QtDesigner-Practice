import sys
from PyQt5.QtWidgets import QApplication, QWidget

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "My practice window"
        self.left = 10
        self.top = 10
        self.height = 480
        self.width = 640
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

ex = App()
sys.exit(app.exec())
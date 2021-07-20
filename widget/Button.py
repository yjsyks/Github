
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class PushsButton(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton demo")
        self.vbox = QVBoxLayout()

        self.setLayout(self.vbox)
        self.btnText=QPushButton(self)
        self.btnhtnl

        self.BtnText.clicked.connect(self.onClick_BtnText)
        self.BtnHtml.clicked.connect(self.onClick_BtnHtml)
        self.BtntoText.clicked.connect(self.onClick_BtntoText)
        self.BtntoHtml.clicked.connect(self.onClick_BtntoHtml)

    def onClick_BtnText(self):
        self.edit1.setPlainText("Hello world,世界你好")

    def onClick_BtnHtml(self):
        self.edit1.setHtml(
            '<font color="blue" size="5">Hello world,世界你好</font>')

    def onClick_BtntoText(self):
        print(self.edit1.toPlainText())

    def onClick_BtntoHtml(self):
        print(self.edit1.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PushsButton()
    main.show()
    sys.exit(app.exec_())

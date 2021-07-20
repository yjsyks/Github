'''
多窗口交互
不使用信号与槽

win1 和 win2 相互交互
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from DateDialog import DateDialog


class DateDialog(QDialog):
    pass


class MultiWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton demo")
        self.resize(300, 200)
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindow()
    main.show()
    sys.exit(app.exec_())

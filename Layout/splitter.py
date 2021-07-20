import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Createlayout(QWidget):
    def __init__(self):
        super(Createlayout, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("栅格布局：表单设计")
        self.resize(500, 400)

        hbox = QHBoxLayout()

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        btn = QPushButton(topleft)
        btn.setText('按钮1')
        btn.move(30, 30)

        splitter1 = QSplitter(Qt.Horizontal)
        textedt = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedt)
        splitter1.setSizes([100, 200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)

        vbox = QHBoxLayout(bottom)
        vbox.addWidget(QPushButton('123'))
        vbox.addWidget(QPushButton('222'))

        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Createlayout()
    main.show()
    sys.exit(app.exec_())

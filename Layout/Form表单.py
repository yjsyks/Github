import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Createmenudemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("垂直盒布局")
        self.resize(300, 300)

        grid = QGridLayout()

        labelbookname = QLabel('标题')
        lntook = QLineEdit()

        labelAutor = QLabel('作者')
        lntAutor = QLineEdit()

        labelcontent = QLabel('内容')
        lntcontent = QTextEdit()

        grid.setSpacing(10)
        grid.addWidget(labelbookname, 1, 0)
        grid.addWidget(lntook, 1, 1)

        grid.addWidget(labelAutor, 2, 0)
        grid.addWidget(lntAutor, 2, 1)

        grid.addWidget(labelcontent, 3, 0)
        grid.addWidget(lntcontent, 3, 1, 5, 1)

        self.setLayout(grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Createmenudemo()
    main.show()
    sys.exit(app.exec_())

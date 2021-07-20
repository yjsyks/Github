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
        self.resize(300, 200)

        layout = QVBoxLayout()
        ldt = QLineEdit()
        layout.addWidget(ldt)

        grid = QGridLayout()
        layout.addLayout(grid)
        names = ['Cls', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+', ]

        positons = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positons, names):
            if name == "":
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Createmenudemo()
    main.show()
    sys.exit(app.exec_())

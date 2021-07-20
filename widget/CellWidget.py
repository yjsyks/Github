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
        self.setWindowTitle("单元格中放控件")
        self.resize(300, 200)

        layout=QHBoxLayout()




        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Createmenudemo()
    main.show()
    sys.exit(app.exec_())

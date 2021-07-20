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
        #self.resize(300, 200)

        layout = QHBoxLayout()

        layout.addWidget(QPushButton('按钮1'), 1, Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(QPushButton('按钮2'), 1, Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(QPushButton('按钮3'), 1, Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(QPushButton('按钮4'), 1, Qt.AlignLeft | Qt.AlignBottom)
        layout.addWidget(QPushButton('按钮5'), 1, Qt.AlignLeft | Qt.AlignBottom)
        layout.setSpacing(1)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Createmenudemo()
    main.show()
    sys.exit(app.exec_())

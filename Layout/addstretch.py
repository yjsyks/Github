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
        self.resize(400, 500)

        vbox = QVBoxLayout()
        hbox=QHBoxLayout()


        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn4 = QPushButton(self)
        btn5 = QPushButton(self)
        btn1.setText('按钮1')
        btn2.setText('按钮2')
        btn3.setText('按钮3')
        btn4.setText('确定')
        btn5.setText('取消')

        # 垂直布局
        vbox.addStretch(0)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 水平布局 通过设置伸缩量 addStretch 将两个按钮放在右下角
        hbox.addStretch(1)
        hbox.addWidget(btn4)
        hbox.addWidget(btn5)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Createmenudemo()
    main.show()
    sys.exit(app.exec_())

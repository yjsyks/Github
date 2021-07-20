
import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Stackdemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("堆栈控件")
        self.resize(300, 120)


        layout = QHBoxLayout()

        self.list=QListWidget()
        self.list.insertItem(0,"联系方式")
        self.list.insertItem(1, "个人信息")
        self.list.insertItem(2, "教育程度")


        self.tab1=QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.stack=QStackedWidget()
        self.stack.addWidget(self.tab1)
        self.stack.addWidget(self.tab2)
        self.stack.addWidget(self.tab3)


        layout.addWidget(self.list)
        layout.addWidget(self.stack)

        self.setLayout(layout)

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.list.currentRowChanged.connect(self.display)


    def tab1UI(self):
        layout=QFormLayout()
        layout.addRow("姓名",QLineEdit())
        layout.addRow("地址", QLineEdit())

        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton("1"))
        sex.addWidget(QRadioButton("2"))
        layout.addRow(QLabel("性别"),sex)
        layout.addRow(QLabel("生日"),QLineEdit())

        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("语文"))
        layout.addWidget(QCheckBox("数学"))

        self.tab3.setLayout(layout)

    def display(self,index):
        self.stack.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Stackdemo()
    main.show()
    sys.exit(app.exec_())


import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class TabWidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("选项卡控件")
        self.resize(300, 120)
        layout = QHBoxLayout()

        self.tabWidget=QTabWidget()
        self.tab1=QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabWidget.addTab(self.tab1,"选项卡1")
        self.tabWidget.addTab(self.tab2, "选项卡2")
        self.tabWidget.addTab(self.tab3, "选项卡3")

        layout.addWidget(self.tabWidget)
        self.setLayout(layout)

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        layout=QFormLayout()
        layout.addRow("姓名",QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.tabWidget.setTabText(0,'联系方式')
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton("1"))
        sex.addWidget(QRadioButton("2"))
        layout.addRow(QLabel("性别"),sex)
        layout.addRow(QLabel("生日"),QLineEdit())
        self.tabWidget.setTabText(1,'个人详细信息')
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("语文"))
        layout.addWidget(QCheckBox("数学"))

        self.tabWidget.setTabText(2,'科目')
        self.tab3.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TabWidgetDemo()
    main.show()
    sys.exit(app.exec_())

'''
Author: your name
Date: 2021-06-09 18:58:52
LastEditTime: 2021-06-11 20:52:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \WxPython\HYXY\calendar.py
'''
import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CalendarDemo(QWidget):
    def __init__(self):
        
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("日历控件演示")
        self.resize(400, 400)

        self.cl = QCalendarWidget(self)
        self.cl.setGridVisible(True)
        self.cl.setMinimumDate(QDate(1980,1,1))
        self.cl.setMaximumDate(QDate(2030,1,1))
        # date = self.cl.selectedDate()
        self.cl.move(20, 20)
        self.cl.clicked.connect(self.showDate)

        self.label = QLabel(self)
        self.label.setText(self.cl.selectedDate().toString("yyyy-MM-dd dddd"))
        self.label.move(20, 300)

    def showDate(self):
        self.label.setText(self.cl.selectedDate().toString("yyyy-MM-dd dddd"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CalendarDemo()
    main.show()
    sys.exit(app.exec_())

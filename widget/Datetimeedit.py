import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DatetimeEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("日历控件演示")
        self.resize(300, 200)

        layout=QVBoxLayout()

        DatetimeEdit1=QDateTimeEdit()
        DatetimeEdit2=QDateTimeEdit(QDateTime.currentDateTime())
        dateedit=QDateEdit(QDate.currentDate())
        timeedit=QTimeEdit(QTime.currentTime())

        DatetimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        DatetimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        DatetimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))

        DatetimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
        DatetimeEdit2.setCalendarPopup(True)


        dateedit.setDisplayFormat("yyyy.MM.dd")
        timeedit.setDisplayFormat("HH:mm:ss")



        layout.addWidget(DatetimeEdit1)
        layout.addWidget(DatetimeEdit2)
        layout.addWidget(dateedit)
        layout.addWidget(timeedit)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DatetimeEditDemo()
    main.show()
    sys.exit(app.exec_())

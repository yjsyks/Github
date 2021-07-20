import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CellFontColor(QWidget):
    def __init__(self):
        super().__init__()
        self.orderType = Qt.DescendingOrder
        self.initUI()

    def initUI(self):
        self.setWindowTitle("日历控件演示")
        self.resize(400, 300)
        layout = QVBoxLayout()
        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount(4)
        self.tablewidget.setColumnCount(3)
        layout.addWidget(self.tablewidget)
        self.tablewidget.setHorizontalHeaderLabels(["姓名", "性别", "体重(kg)"])

        newitem = QTableWidgetItem("张三")
        self.tablewidget.setItem(0, 0, newitem)

        newitem = QTableWidgetItem("男")
        self.tablewidget.setItem(0, 1, newitem)

        newitem = QTableWidgetItem("120")
        self.tablewidget.setItem(0, 2, newitem)

        newitem = QTableWidgetItem("李四")
        self.tablewidget.setItem(1, 0, newitem)

        newitem = QTableWidgetItem("男")
        self.tablewidget.setItem(1, 1, newitem)

        newitem = QTableWidgetItem("112")
        self.tablewidget.setItem(1, 2, newitem)

        newitem = QTableWidgetItem("王五")
        self.tablewidget.setItem(2, 0, newitem)

        newitem = QTableWidgetItem("男")
        self.tablewidget.setItem(2, 1, newitem)

        newitem = QTableWidgetItem("140")
        self.tablewidget.setItem(2, 2, newitem)

        self.button = QPushButton('排序')
        self.button.clicked.connect(self.sortItems)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def sortItems(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder

        self.tablewidget.sortItems(2,self.orderType)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellFontColor()
    main.show()
    sys.exit(app.exec_())

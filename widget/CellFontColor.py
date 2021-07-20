import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CellFontColor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("日历控件演示")
        self.resize(500, 300)
        layout = QHBoxLayout()
        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(4)
        layout.addWidget(tablewidget)
        tablewidget.setHorizontalHeaderLabels(["姓名", "性别", "体重(kg)","显示图片"])

        newitem = QTableWidgetItem("雷神")
        newitem.setTextAlignment(Qt.AlignCenter )
        newitem.setFont(QFont("Times", 12, QFont.Black))
        newitem.setForeground(QBrush(QColor(255, 0, 0)))
        tablewidget.setItem(0, 0, newitem)

        newitem = QTableWidgetItem("男")
        newitem.setTextAlignment(Qt.AlignCenter )
        newitem.setFont(QFont("Times", 12, QFont.Black))
        newitem.setForeground(QBrush(QColor(0, 0, 255)))
        tablewidget.setItem(0, 1, newitem)

        newitem = QTableWidgetItem("160")
        newitem.setTextAlignment(Qt.AlignCenter )
        newitem.setFont(QFont("Times", 12, QFont.Black))
        newitem.setForeground(QBrush(QColor(0, 0, 255)))
        tablewidget.setItem(0, 2, newitem)


        newitem = QTableWidgetItem(QIcon('../hyDM/images/exit.png'), "退出")
        newitem.setFont(QFont("Times", 12, QFont.Black))
        tablewidget.setItem(0, 3, newitem)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellFontColor()
    main.show()
    sys.exit(app.exec_())

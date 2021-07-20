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
        self.setWindowTitle("Cell查找")
        self.resize(600, 800)

        layout = QHBoxLayout()

        tablewidget = QTableWidget()
        tablewidget.setRowCount(80)
        tablewidget.setColumnCount(4)
        layout.addWidget(tablewidget)

        for i in range(80):
            for j in range(4):
                itemcount = "(%d,%d)" % (i, j)
                tablewidget.setItem(i, j, QTableWidgetItem(itemcount))

        # 查找内容
        text = "6,3)"
        # 用finditems获得查找的内容，返回到列表中
        items = tablewidget.findItems(text, Qt.MatchEndsWith)
        if len(items) > 0:
            for item in items:
                item.setBackground(QBrush(QColor(0, 255, 0)))
                item.setForeground(QBrush(QColor(255, 0, 0)))
                # 获得当前行
                row = item.row()
                # 定位到指定行，将滚轮滚到当前行
                tablewidget.verticalScrollBar().setSliderPosition(row)

        self.setLayout(layout)

    def modiAge(self):
        age, ok = QInputDialog.getText(self, "修改年龄", "输入年龄(岁)：")
        if ok:
            self.modiBTN.setText(age)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Createmenudemo()
    main.show()
    sys.exit(app.exec_())

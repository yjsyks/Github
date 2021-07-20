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
        self.setWindowTitle("TabelWidget控件演示")
        self.resize(300, 200)

        layout=QHBoxLayout()

        tablewidget=QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)
        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(["姓名","性别",'年龄'])

        item1=QTableWidgetItem("小明")
        tablewidget.setItem(0,0,item1)

        cb=QComboBox()
        cb.addItem("男")
        cb.addItem('女')
        cb.addItem('中')
        # QSS
        cb.setStyleSheet('QComboBox{margin:3px};')
        tablewidget.setCellWidget(0,1,cb)

        self.modiBTN=QPushButton("修改")
        self.modiBTN.setDown(True)
        self.modiBTN.setStyleSheet('QPushButton{margin:3px};')
        tablewidget.setCellWidget(0, 2,self.modiBTN)
        self.modiBTN.clicked.connect(self.modiAge)

        # 按照行列内容重置宽度
        #tablewidget.resizeColumnsToContents()
        #tablewidget.resizeRowsToContents()


        # 显示或隐藏表头
        tablewidget.horizontalHeader().setVisible(True)
        tablewidget.verticalHeader().setVisible(True)

        # 设置列显示
        tablewidget.setVerticalHeaderLabels(['a','b','c','d'])


        # 设置隐藏或者显示表格线
        tablewidget.setShowGrid(True)

        self.setLayout(layout)


    def modiAge(self):
        age,ok=QInputDialog.getText(self,"修改年龄","输入年龄(岁)：")
        if ok:
            self.modiBTN.setText(age)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Createmenudemo()
    main.show()
    sys.exit(app.exec_())

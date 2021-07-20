import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CellSKJ(QWidget):
    def __init__(self):
        super().__init__()
        self.orderType = Qt.DescendingOrder
        self.initUI()

    def initUI(self):
        self.setWindowTitle("日历控件演示")
        self.resize(400, 300)
        layout1 = QHBoxLayout()

        addbtn=QPushButton("添加节点")
        modbtn=QPushButton("修改节点")
        delbtn = QPushButton("删除节点")

        layout1.addWidget(addbtn)
        layout1.addWidget(modbtn)
        layout1.addWidget(delbtn)

        addbtn.clicked.connect(self.addnode)
        modbtn.clicked.connect(self.modnode)
        delbtn.clicked.connect(self.delnode)


        mainlayout=QVBoxLayout()
        mainlayout.addLayout(layout1)



        self.tree=QTreeWidget()
        self.tree.setColumnCount(2)

        mainlayout.addWidget(self.tree)

        self.tree.setHeaderLabels(["key","value"])

        # 添加根节点
        root=QTreeWidgetItem(self.tree)
        self.tree.setColumnWidth(0,200)
        root.setText(0,"根节点")
        root.setIcon(0, QIcon("../hyDM/images/exit.png"))

        # 添加子节点1
        child1=QTreeWidgetItem(root)
        child1.setText(0,"子节点1")
        child1.setText(1,"节点1的值")
        child1.setCheckState(0,Qt.Checked)
        # 添加子节点2
        child2=QTreeWidgetItem(root)
        child2.setText(0,"子节点2")
        child2.setText(1,"节点2的值")

        child3=QTreeWidgetItem(child1)
        child3.setText(0,"子节点1-1")
        child3.setText(1,"节点1-1的值")

        child4=QTreeWidgetItem(child3)
        child4.setText(0,"子节点1-1-1")
        child4.setText(1,"节点1-1-1的值")

        self.tree.clicked.connect(self.onTreeclicked)

        self.tree.expandAll()  # 设置全部展开模式
        self.setLayout(mainlayout)

    def onTreeclicked(self,index):
        item=self.tree.currentItem()
        print(index.row())
        print("key=%s,value=%s" %(item.text(0),item.text(1)))


    def addnode(self):
        print("添加节点")
        item=self.tree.currentItem()
        node=QTreeWidgetItem(item)
        node.setText(0,"新节点")
        node.setText(1, "新值")


    def modnode(self):
        print("修改节点")
        item = self.tree.currentItem()
        item.setText(0, "修改节点")
        item.setText(1, "值已被修改")

    def delnode(self):
        print("删除节点")
        item = self.tree.currentItem()
        root=self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            if item.parent()!= None: #如果父节点不为空
                item.parent().removeChild(item)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellSKJ()
    main.show()
    sys.exit(app.exec_())

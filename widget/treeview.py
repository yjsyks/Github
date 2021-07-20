
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
        self.setWindowTitle("Treeview控件演示")
        self.resize(600, 400)
        layout = QHBoxLayout()
        model=QDirModel()
        tree=QTreeView()
        tree.setModel(model)

        layout.addWidget(tree)


        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Createmenudemo()
    main.show()
    sys.exit(app.exec_())

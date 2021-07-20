import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Createmenudemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("日历控件演示")
        self.resize(300, 200)
        

        bar=self.menuBar()
        menu=bar.addMenu("文件")
        open=menu.addAction("打开")
        save=QAction("保存",self)
        save.setShortcut("Ctrl+s")
        menu.addAction(save)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Createmenudemo()
    main.show()
    sys.exit(app.exec_())

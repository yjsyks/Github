
import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd


class MultiWindows(QMainWindow):
    count=0
    def __init__(self,parent=None):
        super(MultiWindows,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MDI多窗口")
        self.resize(800,600)

        #layout = QHBoxLayout()

        self.mdi=QMdiArea()
        #layout.addWidget(self.mdi)

        self.setCentralWidget(self.mdi)

        bar=self.menuBar()
        file=bar.addMenu("File")
        file.addAction("new")
        file.addAction('acasade')
        file.addAction('titled')
        file.triggered.connect(self.subWindow)

        #self.setLayout(layout)

    def subWindow(self,q):
        print(q.text())
        if q.text() == "new":
            MultiWindows.count=MultiWindows.count+1
            sub=QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口"+str(MultiWindows.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == "acasade":
            self.mdi.cascadeSubWindows()
        elif q.text() == "titled":
            self.mdi.tileSubWindows()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindows()
    main.show()
    sys.exit(app.exec_())

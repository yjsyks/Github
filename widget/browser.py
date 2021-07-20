import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import os


class WinTimer(QWidget):
    def __init__(self, parent=None):
        super(WinTimer, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("滚动条控件演示")
        # self.resize(400, 300)
        self.setGeometry(300, 300, 800, 600)
        layout=QHBoxLayout()

        self.browser=QWebEngineView()
        # self.browser.load(QUrl('https://www.jd.com'))
        #self.setCentralWidget(self.browser)
        url=os.getcwd()+"/test.html"
        self.browser.load(QUrl.fromLocalFile(url))

        layout.addWidget(self.browser)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WinTimer()
    main.show()
    sys.exit(app.exec_())

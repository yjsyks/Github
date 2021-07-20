import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QVBoxLayout, QWidget, QLabel, QToolTip
from PySide2.QtGui import QIcon, QFont, QPixmap, QPalette
from PySide2.QtCore import Qt


class Qlabelwin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建4个label标签
        self.label1 = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()
        self.label4 = QLabel()

        self.label1.setText("<font color=yellow>这是一个文本标签</font>")
        self.label1.setAutoFillBackground(True)  # 自动填充
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        self.label1.setPalette(palette)
        self.label1.setAlignment(Qt.AlignCenter)

        self.label2.setText("<a href=#>欢迎使用Python Gui程序</a>")

        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setToolTip("这是一个图片标签")
        self.label3.setPixmap(QPixmap("../hyDM/images/loadtest.png"))

        self.label4.setOpenExternalLinks(True)
        self.label4.setText("<a href='http://www.baidu.com'>百度搜索</a>")
        self.label4.setAlignment(Qt.AlignRight)

        self.label2.linkHovered.connect(self.linkhoverd)
        self.label4.linkActivated.connect(self.onclicked)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.label2)
        self.vbox.addWidget(self.label3)
        self.vbox.addWidget(self.label4)

        self.setLayout(self.vbox)
        self.setWindowTitle("123123")

    def linkhoverd(self):
        print("当鼠标划过标签时，触发事件")

    def onclicked(self):
        print("当鼠标点击标签时，触发事件")

        # 创建1个窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("favicon.ico"))
    main = Qlabelwin()
    main.show()
    sys.exit(app.exec_())

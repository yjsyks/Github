import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QDesktopWidget,QHBoxLayout,QWidget,QPushButton,QToolTip
from PySide2.QtGui import QIcon,QFont


class Tooltip(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("微软雅黑",12))
        self.setToolTip("今天是<b>星期日</b>")
        self.setGeometry(300,300,280,280)
        self.setWindowTitle("121")

        self.Button1 = QPushButton("退出当前程序")
        self.Button1.setToolTip("这TM绝对是来捣乱的")
        layout = QHBoxLayout()  # 创建1个布局
        layout.addWidget(self.Button1)  # 将按钮放到布局中

        # 创建1个窗口
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)  # 主程序设置mainFrame


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("favicon.ico"))
    main = Tooltip()
    main.show()
    sys.exit(app.exec_())

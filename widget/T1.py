import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QDesktopWidget,QHBoxLayout,QWidget,QPushButton
from PySide2.QtGui import QIcon


class FirstMainwin(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口标题
        self.setWindowTitle("窗口居中")
        self.resize(400, 300)
        self.status = self.statusBar()
        self.status.showMessage("5秒的信息", 5000)
        self.center()  # 调用窗口居中

        self.Button1=QPushButton("退出当前程序")
        self.Button1.clicked.connect(self.onClick)

        layout=QHBoxLayout() # 创建1个布局
        layout.addWidget(self.Button1) #将按钮放到布局中

        #创建1个窗口
        mainFrame=QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)  #主程序设置mainFrame


    # 让窗口居中
    def center(self):
        # 获取屏幕的尺寸
        screen = QApplication.desktop()
        # 获得窗口的尺寸
        size = self.geometry()
        newleft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2

        self.move(newleft, newTop)

    def onClick(self):
        sender=self.sender()
        print(sender.text() + "按钮被按下")
        app=QApplication.instance()  #获取当前APP的实例化对象
        app.quit()              #app 退出


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("favicon.ico"))
    main = FirstMainwin()
    main.show()
    sys.exit(app.exec_())

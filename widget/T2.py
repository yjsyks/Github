import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__(parent)

        # 设置主窗口标题
        self.setWindowTitle('设置主窗口位置')
        # 设置主窗口大小
        self.resize(400, 300)
        # 设置主窗口在屏幕中的位置
        self.move(500, 100)
        self.center()  # 调用窗口居中
        # 添加状态栏
        self.status = self.statusBar()

    def center(self):
        # screenGeometry（）函数提供有关可用屏幕几何的信息
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        window = self.geometry()

        leftlength = (screen.width() - window.width()) / 2
        toplength = (screen.height() - window.height()) / 2

        self.move(leftlength, toplength)

        print(
            f"window.width():{window.width()},window.height():{window.height()}")
        print(f"窗口左间距:{leftlength}，上间距:{toplength}")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(r'./ICON/cartoon2.ico'))

    main = FirstMainWin()

    main.show()

    sys.exit(app.exec_())

import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class Qmessgeboxwin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("消息框Demo")
        self.resize(300, 200)

        self.button = QPushButton(self)
        self.button.setText("打开对话框")
        self.button.move(50, 50)

        self.button.clicked.connect(self.showDialog)

        self.button1 = QPushButton(self)
        self.button1.setText("显示消息对话框")
        self.button1.move(50, 80)

        self.button1.clicked.connect(self.showDialog)

    def showDialog(self):
        text = self.sender().text()
        if text == "打开对话框":
            QMessageBox.about(self, "关于", "打开对话框")
        elif text == "显示消息对话框":
            reply=QMessageBox.information(self, "关于", "显示消息提示框",QMessageBox.Yes | QMessageBox.No)
            print(reply)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Qmessgeboxwin()
    main.show()
    sys.exit(app.exec_())

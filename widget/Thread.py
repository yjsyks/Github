import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

sec = 0


class workThread(QThread):
    timer = pyqtSignal()
    end = pyqtSignal()

    def run(self):
        while True:
            self.sleep(1)
            if sec == 5:
                self.end.emit()
                break
            self.timer.emit()


class WinTimer(QWidget):
    def __init__(self, parent=None):
        super(WinTimer, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('多线程')
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.lcdnumer = QLCDNumber()
        layout.addWidget(self.lcdnumer)

        button = QPushButton('开始')
        layout.addWidget(button)

        self.setLayout(layout)

        self.workthread = workThread()

        self.workthread.timer.connect(self.start)
        self.workthread.end.connect(self.end)
        button.clicked.connect(self.work)

    def start(self):
        global sec
        sec += 1
        self.lcdnumer.display(sec)

    def end(self):
        QMessageBox.information(self, "消息", "停止计数", QMessageBox.Ok)

    def work(self):
        self.workthread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WinTimer()
    main.show()
    sys.exit(app.exec_())

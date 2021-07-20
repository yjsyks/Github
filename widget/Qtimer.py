from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from datetime import datetime


class WinTimer(QWidget):
    def __init__(self, parent=None):
        super(WinTimer, self).__init__(parent)

        ###界面显示
        self.label_start = QLabel("开始时间:")
        self.label_curr = QLabel("当前时间:")
        self.label_total = QLabel("时间总计:")
        self.startBtn = QPushButton("开始")
        self.endBtn = QPushButton("停止")
        self.endBtn.setEnabled(False)

        ##时间变量
        self.start_time = QDateTime.currentDateTime()
        self.stop_time = QDateTime.currentDateTime()

        ###定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.currTime)

        layout = QGridLayout()
        layout.addWidget(self.label_start, 0, 0, 1, 2)
        layout.addWidget(self.label_curr, 1, 0, 1, 2)
        layout.addWidget(self.label_total, 2, 0, 1, 2)
        layout.addWidget(self.startBtn, 3, 0)
        layout.addWidget(self.endBtn, 3, 1)
        self.setLayout(layout)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        self.setWindowTitle("QTimer")
        self.resize(250, 100)

    def currTime(self):
        self.stop_time = QDateTime.currentDateTime()
        str_time = self.stop_time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label_curr.setText("当前时间:" + str_time)

        str_start = self.start_time.toString("yyyy-MM-dd hh:mm:ss")
        str_curr = self.stop_time.toString("yyyy-MM-dd hh:mm:ss")
        startTime = datetime.strptime(str_start, "%Y-%m-%d %H:%M:%S")
        endTime = datetime.strptime(str_curr, "%Y-%m-%d %H:%M:%S")
        seconds = (endTime - startTime).seconds
        self.label_total.setText("时间总计:" + str(seconds) + "s")

    def startTimer(self):
        self.start_time = QDateTime.currentDateTime()
        str_time = self.start_time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label_start.setText("开始时间:" + str_time)
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinTimer()
    form.show()
    sys.exit(app.exec_())

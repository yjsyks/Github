import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt



class DrawLine(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("设置Pen样式")
        self.resize(600, 300)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        # 实线 1
        pen = QPen(Qt.red, 2,Qt.SolidLine)  # 创建1个画笔
        painter.setPen(pen)
        painter.drawLine(20,40,250,40)

        # 实线 2
        pen = QPen(Qt.black, 3, Qt.DashLine)
        #pen.setStyle(Qt.DashLine)  # 创建1个画笔
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        # 实线 3
        pen = QPen(Qt.blue, 5, Qt.DashDotLine)
        #pen.setStyle(Qt.DashDotLine)  # 创建1个画笔
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)


        size = self.size()

        pen=QPen(Qt.red) # 创建1个画笔


        painter.end()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=DrawLine()
    main.show()
    sys.exit(app.exec_())

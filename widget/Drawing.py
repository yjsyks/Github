import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt



class DrawLine(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("画曲线")
        self.resize(300, 300)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()

        for i in range(1000):
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            painter.drawPoint(x, y)

        painter.end()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=DrawLine()
    main.show()
    sys.exit(app.exec_())

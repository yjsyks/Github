import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Scrollbar(QWidget):
    def __init__(self):
        super().__init__()
        self.orderType = Qt.DescendingOrder
        self.initUI()

    def initUI(self):
        self.setWindowTitle("滚动条控件演示")
        # self.resize(400, 300)
        self.setGeometry(300, 300, 400, 300)
        layout = QHBoxLayout()

        self.label = QLabel('Hello world')
        self.label.setFont(QFont("Times",18))
        self.label.setAlignment(Qt.AlignTop)

        layout.addWidget(self.label)


        self.scrollbar1 = QScrollBar()
        self.scrollbar1.setMaximum(255)
        self.scrollbar1.sliderMoved.connect(self.sliderMoved)

        self.scrollbar2 = QScrollBar()
        self.scrollbar2.setMaximum(255)
        self.scrollbar2.sliderMoved.connect(self.sliderMoved)

        self.scrollbar3 = QScrollBar()
        self.scrollbar3.setMaximum(255)
        self.scrollbar3.sliderMoved.connect(self.sliderMoved)

        self.scrollbar4 = QScrollBar()
        self.scrollbar4.setMaximum(255)
        self.scrollbar4.sliderMoved.connect(self.loc)

        layout.addWidget(self.scrollbar1)
        layout.addWidget(self.scrollbar2)
        layout.addWidget(self.scrollbar3)
        layout.addWidget(self.scrollbar4)


        self.setLayout(layout)

        self.y=self.label.pos().y()
        #self.label.move(self.label.x(),self.y-50)

    def sliderMoved(self):
        print(
            self.scrollbar1.value(),
            self.scrollbar2.value(),
            self.scrollbar3.value())
        palette = QPalette()
        c = QColor(
            self.scrollbar1.value(),
            self.scrollbar2.value(),
            self.scrollbar3.value(),
            255)
        palette.setColor(QPalette.Foreground, c)
        self.label.setPalette(palette)

    def loc(self):
        self.label.move(self.label.x(),self.y+self.scrollbar4.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Scrollbar()
    main.show()
    sys.exit(app.exec_())

'''
Author: your name
Date: 2021-07-20 20:51:16
LastEditTime: 2021-07-20 20:51:22
LastEditors: your name
Description: In User Settings Edit
FilePath: \Github\haha\drawing.py
'''
'''
`123`
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np

pixe = 50  # pixels
column = 5  # 列数
raw = 5  # 行数


class Maze(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('确定', self)
        self.origin = np.array([25, 25])  # 生成一个（20，20）的矩阵
        self.img = QPixmap('robot.jpg')
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('画方格示例')
        # self.label.setPixmap(self.img)
        self.update()
        self.btn.move(300, 120)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawGrid(qp)
        qp.end()

    def drawGrid(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        # 用线创建网格
        for c in range(0, column * (pixe + 1), pixe):  # 创建列
            x0, y0, x1, y1 = c, 0, c, column * pixe
            qp.setPen(pen)
            qp.drawLine(x0, y0, x1, y1)
        for r in range(0, raw * (pixe + 1), pixe):  # 创建行
            x0, y0, x1, y1 = 0, r, raw * pixe, r
            qp.setPen(pen)
            qp.drawLine(x0, y0, x1, y1)

        # 在第一格绘制文字
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont("Decorative", 10))
        qp.drawText(0, 0, 30, 30, Qt.AlignCenter, '文字')

        pen = QPen(Qt.white, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(QColor(800, 0, 0))

        # 绘制矩形
        hell1_center = self.origin + np.array([pixe * 2, pixe])
        qp.drawRect(hell1_center[0] - 20, hell1_center[1] - 20, 40,
                    40)  # (起点坐标，终点坐标，长，宽)

        # 绘制一个黄色的圆
        pen = QPen(Qt.yellow, 2, Qt.SolidLine)
        # pen = QPen(QColor(255, 215, 0), 2, Qt.SolidLine)#与上一行代码效果是一样的
        qp.setPen(pen)
        qp.setBrush(QColor(255, 215, 0))
        circle_center = self.origin + np.array([pixe * 2, pixe * 2])
        qp.drawEllipse(circle_center[0] - 20, circle_center[1] - 20, 40, 40)

        # 绘制圆角矩形
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(QColor(255, 0, 0))
        people = self.origin + np.array([0, pixe])
        qp.drawRoundedRect(people[0] - 20, people[1] - 20, 40, 40, 30,
                           15)  # 后边两个参数是圆角的半径


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Maze()
    ex.show()
    sys.exit(app.exec_())

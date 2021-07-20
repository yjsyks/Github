import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# 自定义信号

class MutiSignal(QObject):
    # 自定义信号 定义多个信号
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)
    signal3 = pyqtSignal(int, str)
    signal4 = pyqtSignal(list)
    signal5 = pyqtSignal(dict)
    # 重载信号 ,槽函数的参数可以是int str,也可以是str
    signal6 = pyqtSignal([int, str], [str])

    # 信号触发
    def __init__(self):
        super(MutiSignal, self).__init__()

        self.signal1.connect(self.Mycall1)
        self.signal2.connect(self.Mycall2)
        self.signal3.connect(self.Mycall3)
        self.signal4.connect(self.Mycall4)
        self.signal5.connect(self.Mycall5)
        self.signal6[int, str].connect(self.Mycall6)
        self.signal6[str].connect(self.Mycall6OverLoad)

        self.signal1.emit()
        self.signal2.emit(2)
        self.signal3.emit(2, 'China')
        self.signal4.emit([1, 2, 3, 4, 5])
        self.signal5.emit({'name': 'Ana', "age": 20})
        self.signal6[int, str].emit(2, 'Not load')
        self.signal6[str].emit('overload')

    def Mycall1(self):
        print('Signal1 emit')

    def Mycall2(self, val):
        print('Signal2 emit:', val)

    def Mycall3(self, val, text):
        print('Signal3 emit:', val, text)

    def Mycall4(self, val):
        print('Signal4 emit:', val)

    def Mycall5(self, val):
        print('Signal5 emit:', val)

    def Mycall6(self, val, text):
        print('Signal6 emit:', val, text)

    def Mycall6OverLoad(self, text):
        print('Signal6 OverLoad emit:', text)


if __name__ == '__main__':
    msignal = MutiSignal()

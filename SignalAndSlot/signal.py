import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# 自定义信号

class MySignal(QObject):
    # 自定义信号
    sendmsg=pyqtSignal(object)
    sendmsg1 = pyqtSignal(str,int,int,int)
    # 信号触发
    def run(self):
        self.sendmsg.emit('Hello PyQt5')

    def run1(self):
        self.sendmsg1.emit('Hello',2,3,4)

class Myslot(QObject):
    def get(self,msg):
        print('信息: '+msg)

    def get1(self,msg,a,b,c):
        print('信息: '+msg)
        print(a*b*c)

if __name__ == '__main__':
    send=MySignal()
    slot=Myslot()

    send.sendmsg.connect(slot.get)
    send.run()

    send.sendmsg1.connect(slot.get1)
    send.run1()

import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# 自定义信号

class MySignal(QObject):
    # 自定义信号
    sendmsg=pyqtSignal(object)

    # 信号触发
    def run(self):
        self.sendmsg.emit('Hello PyQt5')

class Myslot(QObject):
    def get(self,msg):
        print('信息:'+msg)


if __name__ == '__main__':
    send=MySignal()
    slot=Myslot()

    send.sendmsg.connect(slot.get)
    send.run()


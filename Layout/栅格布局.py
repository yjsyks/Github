'''
Author: your name
Date: 2021-07-06 08:49:04
LastEditTime: 2021-07-17 22:37:37
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \WxPython\HYXY\Layout\栅格布局.py
'''
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


'''
QSS
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Qssbase(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('画方格示例')
        self.resize(400, 300)
        layout = QVBoxLayout()

        btn1 = QPushButton('按钮1')
        btn1.setProperty('name','btn1')
        btn2 = QPushButton('按钮2')
        btn2.setProperty('name', 'btn2')

        layout.addWidget(btn1)
        layout.addWidget(btn2)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Qssbase()
    qssstyle = '''
        QPushButton[name="btn2"] {
        Background-color:red;
        color:yellow;
        height:60;
        font-size:30px;
    }
        QPushButton[name="btn1"] {
        Background-color:blue;
        color:red;
        height:60;
        font-size:30px;
    }
    '''
    ex.setStyleSheet(qssstyle)
    ex.show()
    sys.exit(app.exec_())

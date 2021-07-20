import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon


class Text_Edit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本控件操作")
        self.resize(300,320)

        self.edit1=QTextEdit()
        self.BtnText=QPushButton("显示文本")
        self.BtntoText = QPushButton("获取文本")
        self.BtnHtml=QPushButton('显示HTML')
        self.BtntoHtml = QPushButton('获取HTML')



        layout = QVBoxLayout()
        layout.addWidget(self.edit1)
        layout.addWidget(self.BtnText)
        layout.addWidget(self.BtntoText)
        layout.addWidget(self.BtnHtml)
        layout.addWidget(self.BtntoHtml)
        self.setLayout(layout)

        self.BtnText.clicked.connect(self.onClick_BtnText)
        self.BtnHtml.clicked.connect(self.onClick_BtnHtml)
        self.BtntoText.clicked.connect(self.onClick_BtntoText)
        self.BtntoHtml.clicked.connect(self.onClick_BtntoHtml)

    def onClick_BtnText(self):
        self.edit1.setPlainText("Hello world,世界你好")

    def onClick_BtnHtml(self):
        self.edit1.setHtml('<font color="blue" size="5">Hello world,世界你好</font>')

    def onClick_BtntoText(self):
        print(self.edit1.toPlainText())

    def onClick_BtntoHtml(self):
        print(self.edit1.toHtml())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Text_Edit()
    main.show()
    sys.exit(app.exec_())

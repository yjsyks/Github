from HYXY.Wxpython.UI.noname import MyFrame1
import xlwings as xw


class MyFrame(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.OpenExcelFile("test.xlsx")

    def OpenExcelFile(self, file):
        self.app = xw.App(visible=True, add_book=False)
        self.app.display_alerts = True
        self.app.screen_updating = True
        self.wb = self.app.books.open(file)
        self.sheet = self.wb.sheets["Sheet1"]

    def LoadData(self, adress):
        result = self.sheet[adress].value
        return result

    def SaveData(self, adress, data):
        self.sheet[adress].value = data

    def DragFomula(self, adress, data):
        self.sheet[adress].value = data

    def m_button1OnButtonClick(self, event):
        self.m_textCtrl1.Value = str(self.LoadData("B1"))

    def m_button2OnButtonClick(self, event):
        data = self.m_textCtrl2.Value
        self.SaveData("D1", data)

    def CloseExcel(self):
        self.wb.save()
        self.wb.close()
        self.app.quit()
        exit()

    def MyFrame1OnClose(self, event):
        self.CloseExcel()
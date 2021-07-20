import wx


class MainFrame(wx.Frame):
    def __init__(self, p, t):
        wx.Frame.__init__(self, id=wx.NewId(), parent=p, title=t)
        self.label1 = wx.StaticText(parent=self,
                                    id=-1,
                                    size=(40, 58),
                                    label=u"地点:",
                                    pos=(20, 40))

        self.list1 = wx.ListBox(parent=self,
                                id=-1,
                                size=(60, 300),
                                pos=(100, 10),
                                choices=[u"北京", u"上海", u"广州", u"深圳"])




if __name__ == "__main__":
    app = wx.App(False)
    main_frame = MainFrame(None, u"ListBox演示程序")
    main_frame.Show(True)  # 显示主窗口
    app.MainLoop()

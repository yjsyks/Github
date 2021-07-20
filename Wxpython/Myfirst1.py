# -*- coding:utf-8 -*-
import wx


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(
            self,
            None,
            title='132',
            size=(
                761,
                435),
            name='frame',
            style=541072960)
        self.MyFrame1 = wx.Panel(self)
        self.Centre()
        self.Button1 = wx.Button(
            self.MyFrame1, size=(
                89, 24), pos=(
                22, 13), label='按钮', name='button')
        self.Button1.Bind(wx.EVT_BUTTON, self.Button1_press)
        self.listbox1 = wx.ListBox(
            self.MyFrame1, size=(
                106, 324), pos=(
                20, 49), name='listBox', choices=[], style=32)

    def Button1_press(self, event):
        print('Button1,按钮被单击')


class myApp(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True


if __name__ == '__main__':
    app = myApp()
    app.MainLoop()

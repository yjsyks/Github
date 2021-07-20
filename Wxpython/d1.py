# -*- coding:utf-8 -*-
import wx


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(
            self,
            None,
            title='',
            size=(
                751,
                516),
            name='frame',
            style=541072960)
        self.qdck = wx.Panel(self)
        self.Centre()
        self.lbk1 = wx.ListBox(
            self.qdck, size=(
                147, 325), pos=(
                19, 124), name='listBox', choices=[], style=32)
        self.bjk1 = wx.TextCtrl(
            self.qdck, size=(
                709, 32), pos=(
                17, 9), value='小浪底水库淤积测验', name='text', style=256)

        self.bjk2 = wx.TextCtrl(
            self.qdck, size=(
                149, 31), pos=(
                18, 95), value='', name='text', style=0)
        self.bjk2.Bind(wx.EVT_TEXT, self.bjk2_nrbgb)
        self.an1 = wx.Button(
            self.qdck, size=(
                46, 22), pos=(
                19, 52), label='按钮', name='button')
        self.an2 = wx.Button(
            self.qdck, size=(
                42, 22), pos=(
                75, 53), label='按钮', name='button')

    def bjk2_nrbgb(self, event):
        print('bjk2,内容被改变')


class myApp(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True


if __name__ == '__main__':
    app = myApp()
    app.MainLoop()

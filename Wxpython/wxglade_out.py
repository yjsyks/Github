#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Sat May 22 20:16:10 2021
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((860, 763))
        self.SetTitle("frame")

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)

        self.button_1 = wx.Button(self, wx.ID_ANY, "button_1")
        sizer_3.Add(self.button_1, 0, 0, 0)

        self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        sizer_3.Add(self.combo_box_1, 0, 0, 0)

        self.combo_box_2 = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        sizer_3.Add(self.combo_box_2, 0, 0, 0)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)

        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        sizer_4.Add(self.text_ctrl_1, 0, 0, 0)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_4.Add(self.panel_1, 1, wx.EXPAND, 0)

        self.list_box_1 = wx.ListBox(self, wx.ID_ANY, choices=["choice 1"])
        sizer_4.Add(self.list_box_1, 0, 0, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)

        sizer_5.Add((0, 0), 0, 0, 0)

        self.SetSizer(sizer_2)

        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()

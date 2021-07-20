#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Sat May 22 22:49:56 2021
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((614, 511))

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_2 = wx.Panel(self, wx.ID_ANY)
        self.panel_3 = wx.Panel(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle(("小浪底水库淤积测验处理程序"))

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

        sizer_1.Add(self.panel_1, 1, wx.ALL | wx.EXPAND, 8)

        sizer_2.Add(self.button_1, 0, 0, 0)
        sizer_2.Add(self.button_2, 0, 0, 0)
        sizer_2.Add(self.combo_box_1, 0, 0, 0)
        sizer_2.Add(self.combo_box_2, 0, 0, 0)
        sizer_2.Add(self.button_7, 0, 0, 0)
        sizer_2.Add(self.button_3, 0, 0, 0)
        sizer_2.Add(self.button_4, 0, 0, 0)
        sizer_2.Add(self.button_5, 0, 0, 0)
        sizer_2.Add(self.button_6, 0, 0, 0)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, _("D"))
        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, _(u"数据集刷新"))
        self.combo_box_1 = wx.ComboBox(
            self.panel_1, wx.ID_ANY, choices=[
                _("1"), _("2"), _("3")], style=wx.CB_DROPDOWN)
        self.combo_box_1.SetSelection(0)

        self.combo_box_2 = wx.ComboBox(
            self.panel_1, wx.ID_ANY, choices=[
                _("A"), _("B"), _("C")], style=wx.CB_DROPDOWN)
        self.combo_box_2.SetSelection(0)
        self.button_7 = wx.Button(self.panel_1, wx.ID_ANY, _("PDF"))
        self.button_3 = wx.ToggleButton(self.panel_1, wx.ID_ANY, _(u"测时水位"))
        self.button_4 = wx.ToggleButton(self.panel_1, wx.ID_ANY, _(u"显示测点"))
        self.button_5 = wx.ToggleButton(self.panel_1, wx.ID_ANY, _(u"网格"))
        self.button_6 = wx.ToggleButton(self.panel_1, wx.ID_ANY, _("button_6"))

        sizer_1.Add(self.panel_2, 6, wx.ALL | wx.EXPAND, 3)
        sizer_1.Add(self.panel_3, 1, wx.EXPAND, 0)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_3, wx.ID_ANY, "")
        sizer_3.Add(self.text_ctrl_1, 2, wx.ALL, 0)

        self.panel_3.SetSizer(sizer_3)

        self.panel_1.SetSizer(sizer_2)

        self.SetSizer(sizer_1)

        self.Layout()
        # end wxGlade

# end of class MyFrame


class MyApp(wx.App):
    def OnInit(self):
        self.frame_1 = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame_1)
        self.frame_1.Show()
        return True

# end of class MyApp


if __name__ == "__main__":
    gettext.install("app")  # replace with the appropriate catalog name

    app = MyApp(0)
    app.MainLoop()

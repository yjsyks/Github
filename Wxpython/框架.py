import wx
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
import matplotlib.pyplot as plt


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1119, 728))

        self.function_area = wx.TextCtrl(
            self, wx.ID_ANY, u"水库河道冲淤计算分析系统\n套绘图浏览-主测次模式", style=wx.TE_CENTRE)
        self.Gauge = wx.Gauge(self, wx.ID_ANY)
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY)
        self.pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.data_browser = wx.Button(self.pane_1, wx.ID_ANY, "D")
        self.refresh = wx.Button(self.pane_1, wx.ID_ANY, u"数据集刷新")
        self.reach_selector = wx.Choice(self.pane_1, wx.ID_ANY, choices=[])
        self.mtime_selector = wx.Choice(self.pane_1, wx.ID_ANY, choices=[])
        self.pdf = wx.Button(self.pane_1, wx.ID_ANY, "PDF")
        self.MtimeLevel = wx.ToggleButton(self.pane_1, wx.ID_ANY, u"测时水位")
        self.marker = wx.ToggleButton(self.pane_1, wx.ID_ANY, u"显示测点")
        self.hasgrid = wx.ToggleButton(self.pane_1, wx.ID_ANY, u"网格")
        self.haslegend = wx.ToggleButton(self.pane_1, wx.ID_ANY, u"图例")
        self.toolbar = ()
        self.search = wx.TextCtrl(self.pane_1, wx.ID_ANY, "")
        self.section_list = wx.ListBox(self.pane_1, wx.ID_ANY, choices=[])
        self.figure = Figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.pane_1, wx.ID_ANY, self.figure)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
        self.mtime_list = wx.CheckListBox(
            self.pane_1, wx.ID_ANY, choices=[], style=wx.LB_EXTENDED | wx.LB_NEEDED_SB)
        self.log = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE)

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(u"套绘图浏览")
        self.function_area.SetMinSize((-1, 50))
        self.function_area.SetFont(wx.Font(
            15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.data_browser.SetMinSize((15, 30))
        self.pdf.SetMinSize((45, 30))
        self.MtimeLevel.SetMinSize((80, 30))
        self.marker.SetMinSize((80, 30))
        self.hasgrid.SetMinSize((40, 30))
        self.haslegend.SetMinSize((40, 30))
        self.search.SetMinSize((120, 25))
        self.section_list.SetMinSize((120, 400))
        self.canvas.SetMinSize((850, 400))
        self.mtime_list.SetMinSize((120, 400))
        self.log.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT,
                                 wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        # end wxGlade
        self.hasgrid.SetValue(True)
        self.haslegend.SetValue(True)

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_pane_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_pane_1_main = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_pane_1_command = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.function_area, 0, wx.ALL | wx.EXPAND, 0)
        sizer_9.Add(self.Gauge, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        sizer_1.Add(sizer_9, 0, wx.EXPAND, 0)
        sizer_pane_1_command.Add(self.data_browser, 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add((3, 20), 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add(self.refresh, 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add((20, 20), 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add(self.reach_selector, 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add((20, 20), 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add(self.mtime_selector, 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add((20, 20), 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add(self.pdf, 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add((20, 20), 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add(self.MtimeLevel, 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add((20, 20), 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add(self.marker, 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add((20, 20), 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add(self.hasgrid, 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add((20, 20), 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add(self.haslegend, 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add((20, 20), 0, wx.ALIGN_CENTER, 0)
        sizer_pane_1_command.Add(self.toolbar, 1, wx.ALIGN_CENTER, 0)
        sizer_pane_1.Add(sizer_pane_1_command, 1, 0, 0)
        sizer_2.Add(self.search, 0, wx.EXPAND, 0)
        sizer_2.Add(self.section_list, 1, wx.EXPAND, 0)
        sizer_pane_1_main.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_pane_1_main.Add(self.canvas, 7, wx.EXPAND, 0)
        sizer_pane_1_main.Add(self.mtime_list, 0,
                              wx.ALIGN_RIGHT | wx.EXPAND, 0)
        sizer_pane_1.Add(sizer_pane_1_main, 15, wx.EXPAND, 0)
        self.pane_1.SetSizer(sizer_pane_1)
        self.notebook_1.AddPage(self.pane_1, u"套绘图")
        sizer_1.Add(self.notebook_1, 6, wx.EXPAND, 0)
        sizer_1.Add(self.log, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        # self.frame.Center()
        self.frame.Show()
        return True

    def OnExit(self):
        return True


# end of class MyApp


if __name__ == "__main__":
    app = MyApp(0)
    # mainframe=app.frame
    app.MainLoop()

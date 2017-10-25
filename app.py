# -*- coding: utf-8 -*- #
import wx
import os
from wavobj import *


class Myapp(wx.Frame):
    def __init__(self, parent, title):
        super(Myapp, self).__init__(parent, title=title)
        self.InitUI()

    def InitUI(self):
        p = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.l1 = wx.StaticText(p, label="文件名", style=wx.ALIGN_LEFT)
        self.l2 = wx.StaticText(p, label="文件参数", style=wx.ALIGN_LEFT)
        vbox.Add(self.l1, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)
        vbox.Add(self.l2, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)
        b1 = wx.Button(p, label="打开")
        vbox.Add(b1, 0, wx.ALIGN_LEFT)

        #b2 = wx.Button(p, label="Plot td")
        #vbox.Add(b2, 0, wx.ALIGN_CENTER_HORIZONTAL)
        #t = wx.TextCtrl(p)
        #vbox.Add(t, 1, wx.EXPAND, 10)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        #l2 = wx.StaticText(p, label="Label2", style=wx.ALIGN_CENTRE)

        #hbox.Add(l2, 0, wx.EXPAND)
        b_td = wx.Button(p, label="开始处理")
        #b_sg = wx.Button(p, label="语图")
        #b_psd = wx.Button(p, label="功率谱密度")
        #b_fd = wx.Button(p, label="频域")
        hbox.AddStretchSpacer(1)
        hbox.Add(b_td, 0, wx.ALIGN_LEFT, 20)
        #hbox.Add(b_sg, 0, wx.ALIGN_LEFT, 20)
        #hbox.Add(b_psd, 0, wx.ALIGN_LEFT, 20)
        #hbox.Add(b_fd, 0, wx.ALIGN_LEFT, 20)
        vbox.Add(hbox, 1, wx.ALL)
        p.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.OnClickb1, b1)
        self.Bind(wx.EVT_BUTTON, self.OnClickb_td, b_td)
        #self.Bind(wx.EVT_BUTTON, self.OnClickb_sg, b_sg)
        #self.Bind(wx.EVT_BUTTON, self.OnClickb_psd, b_psd)
        #self.Bind(wx.EVT_BUTTON, self.OnClickb_fd, b_fd)
        self.Show(True)

    def OnClickb1(self, e):
        wildcard = "Wav Files (*.wav)|*.wav"
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", wildcard, wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.l1.SetLabelText(self.filename)
            self.path = dlg.GetPath()
            self.wav_plot = wavObj(self.path)
            if self.wav_plot.nchannels == 0:
                self.l2.SetLabelText('Can not open this file. Maybe it is compressed.')
            else:
                self.l2.SetLabelText('frames:'+str(self.wav_plot.nframes)+'  framerate:'+str(self.wav_plot.framerate)+'  channels:'+str(self.wav_plot.nchannels))
        dlg.Destroy()


    def OnClickb_td(self, e):
        self.wav_plot.plot_td()
        self.wav_plot.show()

    # def OnClickb_sg(self, e):
    #     self.wav_plot.plot_sg()
    #     self.wav_plot.show()
    #
    # def OnClickb_psd(self, e):
    #     self.wav_plot.plot_psd()
    #     self.wav_plot.show()

    # def OnClickb_fd(self, e):
    #     self.wav_plot.plot_fd()
    #     self.wav_plot.show()

#ex = wx.App()
#Myapp(None, 'wav文件处理程序')
#ex.MainLoop()
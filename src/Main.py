#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import wx
import Frame
if __name__ == '__main__':
    app = wx.App() 
    window = Frame.MyFrame1(None) 
    window.Show(True) 
    app.MainLoop() 
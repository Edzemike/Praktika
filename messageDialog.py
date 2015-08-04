__author__ = 'Edita'
import wx

class calculus (wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Resistance calculator', size=(300, 200)) #sukuriamas langas
        panel = wx.Panel(self) #sukuriama panele


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = calculus(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

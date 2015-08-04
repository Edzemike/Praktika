__author__ = 'Edita'
import wx

class calculus (wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Resistance calculator', size=(500, 200)) #sukuriamas langas
        panel = wx.Panel(self) #sukuriama panele

        status = self.CreateStatusBar()
        menubar = wx.MenuBar()
        pasirinkimai = wx.Menu()
        pasirinkimai.Append(wx.NewId(), 'Get resistor color-code',
                            "In this mode you will find out the code of exact value.")
        menubar.Append(pasirinkimai, 'Change calculator mode')
        self.SetMenuBar(menubar)

        mygtukas = wx.Button(panel, label="4 Band-Code", pos=(15, 20), size = (76, 30)) #sukuriamas mygtukas
        mygtukas1 = wx.Button(panel, label="5 Band-Code", pos=(90, 20), size = (76, 30)) #sukuriamas mygtukas
        mygtukas2 = wx.Button(panel, label="6 Band-Code", pos=(165, 20), size = (76, 30)) #sukuriamas mygtukas
        self.Bind(wx.EVT_BUTTON, self.calcfour, mygtukas) #mygtukui priskiriama funkcija
        self.Bind(wx.EVT_BUTTON, self.calcfive, mygtukas1)
        self.Bind(wx.EVT_BUTTON, self.calcsix, mygtukas2)
        self.Bind(wx.EVT_CLOSE, self.closewindow) #mygtukui x priskiriama uzdarymo funkcija

    def calcfour (self, event):
        pass

    def calcfive (self, event):
        pass

    def calcsix (self, event):
        pass

    def closewindow (self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = calculus(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

from argparse import _ActionsContainer

__author__ = 'Edita'

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import kivy.uix.image
from kivy.lang import Builder
import kivy.uix.gridlayout

Builder.load_file("pagr.kv")


class Tabbedpanel (TabbedPanel):

    def visimygtukai(self, btn1, btn2, btn3):
        btn1 = self.keturiosj
        btn2 = self.penkiosj
        btn3 = self.sesiosj
        btnres1 = self.VarzMyg1
        btnres2 = self.VarsMyg2
        btnres3 = self.Varzmyg3
        btnres4 = self.VarzMyg4
        btnres5 = self.VarzMyg5
        btnres6 = self.VarzMyg6

    def fourbandcode(self):

        print("hi")
        return self

    def fivebandcode (self):
        print("five!")

    def sixbandcode (self):
        print("oh no! You have six fingers!")

    def rezultatas (lst):
        lst = ["a", "b", "c"]#sudarys is mygtuku gauti duomenys
        teksts = ' / '.join(lst)
        return teksts


class MainApp(App):
    def build(self):
        return Tabbedpanel()

    def dictionaries (colortabledigits, colortablemultiplier, colortabletolerance, colortabletemp):
        colortabledigits = {"Black": "0", "Brown": "1", "Red": "2", "Orange": "3", "Yellow": "4", "Green": "5",
                    "Blue": "6", "Violet": "7", "Grey": "8", "White": "9"} # 4BandCode pirmos dvi juosteles,
                                                                    # 5 ir 6 bandCode - pirmos trys juosteles
        colortablemultiplier = {"Silver1": 0.01, "Golden1": 0.1, "Black1": 1, "Brown1": 10, "Red1": 100, "Orange1": 1000,
                        "Yellow1": 10000, "Green1": 100000, "Blue1": 1000000, "Violet1": 10000000} # Daugiklis,
                                                    # 4 BandCode trecia juostele, 5 ir 6 BandCode - ketvirta juostele

        colortabletolerance = {"Silver2": "10%", "Golden2": "5%", "Brown2": "1%", "Red2": "2%", "Green2": "0.5%",
                       "Blue2": "0.25%", "Violet2": "0.1%", "Grey2": "0.05%"} # 4j. -4 BC, 5j. - 5,5BC

        colortabletemp = {"Brown3": "100 ppm", "Red3": "50 ppm", "Orange3": "15 ppm", "Yellow": "25 ppm"}
                                                                                            # tik 6BandCodre 6j.

if __name__ == '__main__':
    MainApp().run()

__author__ = 'Edita'

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
import kivy.uix.image
from kivy.lang import Builder
import kivy.uix.gridlayout
Builder.load_file("pagr.kv")


class Tabbedpanel (TabbedPanel):
    pass


class MainApp(App):
    def build(self):
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



        return Tabbedpanel()



if __name__ == '__main__':
    MainApp().run()

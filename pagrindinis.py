__author__ = 'Edita'

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


Builder.load_file("pagr.kv")


class Tabbedpanel(TabbedPanel, GridLayout):


    def popupwindow1(self):
        #spalv = '0, 0, 0, 1'
        layout = GridLayout(cols=4)
        #background_color=(0, 0, 0, 1)

        myg1 = layout.add_widget(Button(background_color=(0, 0, 0, 1), background_normal=''))   # juodas
        myg2 = layout.add_widget(Button(background_color=(.4, .2, 0, 1), background_normal=''))   # rudas
        myg3 = layout.add_widget(Button(background_color=(1, 0, 0, 1), background_normal=''))   # raudonas
        myg4 = layout.add_widget(Button(background_color=(1, .5, 0, 1), background_normal=''))   # oranzinis
        myg5 = layout.add_widget(Button(background_color=(1, 1, 0, 1), background_normal=''))   # geltonas
        myg6 = layout.add_widget(Button(background_color=(0, .6, 0, 1), background_normal=''))   # zalias
        myg7 = layout.add_widget(Button(background_color=(0, 0, 1, 1), background_normal=''))   # melynas
        myg8 = layout.add_widget(Button(background_color=(.4, 0, .4, 1), background_normal=''))   # violetinis
        myg9 = layout.add_widget(Button(background_color=(1, 1, 1, .5), background_normal=''))   # pilkas
        myg10 = layout.add_widget(Button(background_color=(1, 1, 1, 1), background_normal=''))  # baltas

        popup = Popup(title='Choose a color:',
                      content=layout,
                      size_hint=(None, None), size=(200, 200))
        popup.open()
        #return background_color

    def myg1(self):
       background_color=(0, 0, 0, 1)
       print background_color
       return background_color

    def myg12color(self):
        Background_Color=(1, 1, 1, 1)
        return Background_Color

    def popupwindow2(self):
        layout = GridLayout(cols=4)

        myg1 = layout.add_widget(Button(background_color=(0, 0, 0, 1), background_normal=''))   # juodas
        myg2 = layout.add_widget(Button(background_color=(.4, .2, 0, 1), background_normal=''))   # rudas
        myg3 = layout.add_widget(Button(background_color=(1, 0, 0, 1), background_normal=''))   # raudonas
        myg4 = layout.add_widget(Button(background_color=(1, .5, 0, 1), background_normal=''))   # oranzinis
        myg5 = layout.add_widget(Button(background_color=(1, 1, 0, 1), background_normal=''))   # geltonas
        myg6 = layout.add_widget(Button(background_color=(0, .6, 0, 1), background_normal=''))   # zalias
        myg7 = layout.add_widget(Button(background_color=(0, 0, 1, 1), background_normal=''))   # melynas
        myg8 = layout.add_widget(Button(background_color=(.4, 0, .4, 1), background_normal=''))   # violetinis
        myg11 = layout.add_widget(Button(background_color=(.84, .64, .125, 1), background_normal=''))  # auksinis
        myg12 = layout.add_widget(Button(background_color=(1, 1, 1, .7), background_normal=''))  # sidabrinis

        popup = Popup(title='Choose a color:',
                      content=layout,
                      size_hint=(None, None), size=(200, 200))

        layout.bind(on_press=popup.dismiss)
        popup.open()

    def popupwindow3(self):
        layout = GridLayout(cols=3)
        sk = ''
        sk1 = '100'
        myg2 = layout.add_widget(Button(background_color=(.4, .2, 0, 1), background_normal=''))   # rudas
        myg3 = layout.add_widget(Button(background_color=(1, 0, 0, 1), background_normal=''))   # raudonas
        myg6 = layout.add_widget(Button(background_color=(0, .6, 0, 1), background_normal=''))   # zalias
        myg7 = layout.add_widget(Button(background_color=(0, 0, 1, 1), background_normal=''))   # melynas
        myg8 = layout.add_widget(Button(background_color=(.4, 0, .4, 1), background_normal=''))   # violetinis
        myg9 = layout.add_widget(Button(background_color=(1, 1, 1, .5), background_normal=''))   # pilkas
        myg11 = layout.add_widget(Button(background_color=(.84, .64, .125, 1), background_normal=''))  # auksinis
        myg12 = layout.add_widget(Button(background_color=(1, 1, 1, .7), background_normal=''))  # sidabrinis


        popup = Popup(title='Choose a color:',
                      content=layout,
                      size_hint=(None, None), size=(180, 200))

        popup.open()

    def popupwindow4(sk=''):
        layout = GridLayout(cols=2)
        var1 = "100ppm"

        myg2 = layout.add_widget(Button(background_color=(.4, .2, 0, 1), background_normal=''))   # rudas
        myg3 = layout.add_widget(Button(background_color=(1, 0, 0, 1), background_normal=''))   # raudonas
        myg4 = layout.add_widget(Button(background_color=(1, .5, 0, 1), background_normal=''))   # oranzinis
        myg5 = layout.add_widget(Button(background_color=(1, 1, 0, 1), background_normal=''))   # geltonas

        #myg2.on_press(sk=var1)
        popup = Popup(title='Choose a color:',
                      content=layout,
                      size_hint=(None, None), size=(150, 150))
        popup.open()

        return sk

    def rezultatas(lst):
        lst = ["a", "b", "c"]  # sudarys is mygtuku gauti duomenys
        teksts = ' / '.join(lst)
        return teksts


class ResistanceCalculatorApp(App):

    def build(self):
        return Tabbedpanel()

    '''def dictionaries(self):
        colortabledigits = {"Black": "0", "Brown": "1", "Red": "2", "Orange": "3", "Yellow": "4", "Green": "5",
                            "Blue": "6", "Violet": "7", "Grey": "8", "White": "9"}  # 4BandCode pirmos dvi juosteles,
        # 5 ir 6 bandCode - pirmos trys juosteles
        colortablemultiplier = {"Silver1": 0.01, "Golden1": 0.1, "Black1": 1, "Brown1": 10, "Red1": 100,
                                "Orange1": 1000,
                                "Yellow1": 10000, "Green1": 100000, "Blue1": 1000000, "Violet1": 10000000}  # Daugiklis,
        # 4 BandCode trecia juostele, 5 ir 6 BandCode - ketvirta juostele

        colortabletolerance = {"Silver2": "10%", "Golden2": "5%", "Brown2": "1%", "Red2": "2%", "Green2": "0.5%",
                               "Blue2": "0.25%", "Violet2": "0.1%", "Grey2": "0.05%"}  # 4j. -4 BC, 5j. - 5,5BC

        colortabletemp = {"Brown3": "100 ppm", "Red3": "50 ppm", "Orange3": "15 ppm", "Yellow": "25 ppm"}
        # tik 6BandCodre 6j.'''


if __name__ == '__main__':
    ResistanceCalculatorApp().run()

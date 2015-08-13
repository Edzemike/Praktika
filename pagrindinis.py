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
        return Tabbedpanel()


if __name__ == '__main__':
    MainApp().run()

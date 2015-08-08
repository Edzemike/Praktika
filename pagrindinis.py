__author__ = 'Edita'

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_string("""

<pirmas>:
    canvas:
        Color:
            rgba: (1, 1, 1, .8)
        Rectangle:
            size: self.size
            pos: self.pos
    size_hint: 1, 1 #procentai: 1 - 100%, .5 - 50%
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        canvas:
            Color:
                rgba: (1, 1, 1, .6)
            Rectangle:
                size: self.size
                pos: self.pos
        text: 'Value'
        RstDocument:
            text:
                "Calculates the resistance value according to color-code."
    TabbedPanelItem:
        canvas:
            Color:
                rgba: (1, 1, 1, .6)
            Rectangle:
                size: self.size
                pos: self.pos
        text: 'Colour'
        RstDocument:
            text:
                "Calculates the color-code according to the value of the resistance."
""")


class pirmas(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return pirmas()

if __name__ == '__main__':
    TabbedPanelApp().run()
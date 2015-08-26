__author__ = 'Edita'

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


Builder.load_file("pagr.kv")

#lbl1 = Label(text='', size_hint=(.15, .1), pos_hint={"x": .28, "y": .76}, background_color=(1, 1, 1, .3))
#text1 = TextInput(text='', multiline=False, size_hint=(.15, .06), pos_hint={"x": .02, "y": .7})


class Tabbedpanel(TabbedPanel, GridLayout):
    def popupwindow1(self):
        # spalv = '0, 0, 0, 1'
        layout = GridLayout(cols=4)
        # background_color=(0, 0, 0, 1)

        myg1 = layout.add_widget(Button(background_color=(0, 0, 0, 1), background_normal=''))  # juodas
        myg2 = layout.add_widget(Button(background_color=(.4, .2, 0, 1), background_normal=''))  # rudas
        myg3 = layout.add_widget(Button(background_color=(1, 0, 0, 1), background_normal=''))  # raudonas
        myg4 = layout.add_widget(Button(background_color=(1, .5, 0, 1), background_normal=''))  # oranzinis
        myg5 = layout.add_widget(Button(background_color=(1, 1, 0, 1), background_normal=''))  # geltonas
        myg6 = layout.add_widget(Button(background_color=(0, .6, 0, 1), background_normal=''))  # zalias
        myg7 = layout.add_widget(Button(background_color=(0, 0, 1, 1), background_normal=''))  # melynas
        myg8 = layout.add_widget(Button(background_color=(.4, 0, .4, 1), background_normal=''))  # violetinis
        myg9 = layout.add_widget(Button(background_color=(1, 1, 1, .5), background_normal=''))  # pilkas
        myg10 = layout.add_widget(Button(background_color=(1, 1, 1, 1), background_normal=''))  # baltas

        popup = Popup(title='Choose a color:',
                      content=layout,
                      size_hint=(None, None), size=(200, 200))
        popup.open()
        # return background_color

    def myg1(self):
        background_color = (0, 0, 0, 1)
        print background_color
        return background_color

    def myg12color(self):
        Background_Color = (1, 1, 1, 1)
        return Background_Color

    def popupwindow2(self):
        layout = GridLayout(cols=4)

        myg1 = layout.add_widget(Button(background_color=(0, 0, 0, 1), background_normal=''))  # juodas
        myg2 = layout.add_widget(Button(background_color=(.4, .2, 0, 1), background_normal=''))  # rudas
        myg3 = layout.add_widget(Button(background_color=(1, 0, 0, 1), background_normal=''))  # raudonas
        myg4 = layout.add_widget(Button(background_color=(1, .5, 0, 1), background_normal=''))  # oranzinis
        myg5 = layout.add_widget(Button(background_color=(1, 1, 0, 1), background_normal=''))  # geltonas
        myg6 = layout.add_widget(Button(background_color=(0, .6, 0, 1), background_normal=''))  # zalias
        myg7 = layout.add_widget(Button(background_color=(0, 0, 1, 1), background_normal=''))  # melynas
        myg8 = layout.add_widget(Button(background_color=(.4, 0, .4, 1), background_normal=''))  # violetinis
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
        myg2 = layout.add_widget(Button(background_color=(.4, .2, 0, 1), background_normal=''))  # rudas
        myg3 = layout.add_widget(Button(background_color=(1, 0, 0, 1), background_normal=''))  # raudonas
        myg6 = layout.add_widget(Button(background_color=(0, .6, 0, 1), background_normal=''))  # zalias
        myg7 = layout.add_widget(Button(background_color=(0, 0, 1, 1), background_normal=''))  # melynas
        myg8 = layout.add_widget(Button(background_color=(.4, 0, .4, 1), background_normal=''))  # violetinis
        myg9 = layout.add_widget(Button(background_color=(1, 1, 1, .5), background_normal=''))  # pilkas
        myg11 = layout.add_widget(Button(background_color=(.84, .64, .125, 1), background_normal=''))  # auksinis
        myg12 = layout.add_widget(Button(background_color=(1, 1, 1, .7), background_normal=''))  # sidabrinis

        popup = Popup(title='Choose a color:',
                      content=layout,
                      size_hint=(None, None), size=(180, 200))

        popup.open()

    def popupwindow4(sk=''):
        layout = GridLayout(cols=2)
        var1 = "100ppm"

        myg2 = layout.add_widget(Button(background_color=(.4, .2, 0, 1), background_normal=''))  # rudas
        myg3 = layout.add_widget(Button(background_color=(1, 0, 0, 1), background_normal=''))  # raudonas
        myg4 = layout.add_widget(Button(background_color=(1, .5, 0, 1), background_normal=''))  # oranzinis
        myg5 = layout.add_widget(Button(background_color=(1, 1, 0, 1), background_normal=''))  # geltonas

        # myg2.on_press(sk=var1)
        popup = Popup(title='Choose a color:',
                      content=layout,
                      size_hint=(None, None), size=(150, 150))
        popup.open()

        return sk

    def rezultatas(lst):
        lst = ["a", "b", "c"]  # sudarys is mygtuku gauti duomenys
        teksts = ' / '.join(lst)
        return teksts

    # --------------------------------2-tabas------------------------------

    def values_4band(*args):
        lst = list()
        for arg in args:
            lst.append(arg)

        if lst[1] != '':
            if lst[1].startswith('-'):
                popup = Popup(title='Eror:',
                              content=Label(text="Resistance can not\nbe negative"),
                              size_hint=(None, None), size=(200, 200))
                popup.open()
            sk = float(lst[1])
            if sk < 1:
                print 'pirmas'
                daugiklis = 0.01
                sk = str(int(sk * 100))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 10:
                print 'antras'
                daugiklis = 0.1
                sk = str(int(sk * 10))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 100:
                print 'trecias'
                daugiklis = 1
                sk = str(int(sk))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 1000:
                print 'ketvirtas'
                daugiklis = 10
                sk = str(int(sk / 10))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 10000:
                print 'penktas'
                daugiklis = 100
                sk = str(int(sk / 100))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 100000:
                print 'sestas'
                daugiklis = 1000
                sk = str(int(sk / 1000))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 1000000:
                print 'septintas'
                daugiklis = 10000
                sk = str(int(sk / 10000))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 10000000:
                print 'astuntas'
                daugiklis = 100000
                sk = str(int(sk / 100000))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 100000000:
                print 'devintas'
                daugiklis = 1000000
                sk = str(int(sk / 1000000))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 1000000000:
                print 'desimtas'
                daugiklis = 10000000
                sk = str(int(sk / 10000000))
                s1 = sk[0]
                s2 = sk[1]
            elif sk >= 1000000000:
                popup = Popup(title='Eror:',
                              content=Label(text="Too large number"),
                              size_hint=(None, None), size=(200, 200))
                popup.open()
            ret_daugiklis = 'd' + str(daugiklis)
            ret_s1 = 's1' + str(s1)
            ret_s2 = 's2' + str(s2)
            print ret_daugiklis, ' ', ret_s1, ' ', ret_s2
            ret_list = list()
            ret_list.append(ret_daugiklis)
            ret_list.append(ret_s1)
            ret_list.append(ret_s2)
            te = ' '.join(ret_list)
            print te
            return te  #

    def values_5band(*args):
        lst = list()
        for arg in args:
            lst.append(arg)
        if lst[1] != '':
            if lst[1].startswith('-'):
                popup = Popup(title='Eror:',
                              content=Label(text="Resistance can not\nbe negative"),
                              size_hint=(None, None), size=(200, 200))
                popup.open()
            sk = float(lst[1])

            def priskyrimai(sk, s1=0, s2=0, s3=0):
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
                return s1, s2, s3

            if sk < 0.1:
                daugiklis = 0.01
                sk = str(int(sk*100))
                s1 = 0,
                s2 = 0,
                s3 = sk[0]
            if sk < 1:
                daugiklis = 0.01
                sk = str(int(sk*100))
                s1 = 0
                s2 = sk[0]
                s3 = sk[1]
            elif sk < 10:
                print 'pirmas'
                daugiklis = 0.01
                sk = str(int(sk * 100))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 100:
                print 'antras'
                daugiklis = 0.1
                sk = str(int(sk * 10))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 1000:
                print 'trecias'
                daugiklis = 1
                sk = str(int(sk))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 10000:
                print 'ketvirtas'
                daugiklis = 10
                sk = str(int(sk / 10))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 100000:
                print 'penktas'
                daugiklis = 100
                sk = str(int(sk / 100))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 1000000:
                print 'sestas'
                daugiklis = 1000
                sk = str(int(sk / 1000))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 10000000:
                print 'septintas'
                daugiklis = 10000
                sk = str(int(sk / 10000))
                priskyrimai(sk)
            elif sk < 100000000:
                print 'astuntas'
                daugiklis = 100000
                sk = str(int(sk / 100000))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 1000000000:
                print 'devintas'
                daugiklis = 1000000
                sk = str(int(sk / 1000000))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 10000000000:
                print 'desimtas'
                daugiklis = 10000000
                sk = str(int(sk / 10000000))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk >= 10000000000:
                popup = Popup(title='Eror:',
                              content=Label(text="Too large number"),
                              size_hint=(None, None), size=(200, 200))
                popup.open()

            ret_daugiklis = 'd' + str(daugiklis)
            ret_s1 = 's1' + str(s1)
            ret_s2 = 's2' + str(s2)
            ret_s3 = 's3' + str(s3)
            print ret_daugiklis, ' ', ret_s1, ' ', ret_s2
            ret_list = list()
            ret_list.append(ret_daugiklis)
            ret_list.append(ret_s1)
            ret_list.append(ret_s2)
            ret_list.append(ret_s3)
            te = ' '.join(ret_list)
            print te
            return te

    def s1_color(*args):
        arglst = list()
        for arg in args:
            arglst.append(arg)
        tarp = arglst[1]

        visiTrys = tarp.split()
        juost_1 = visiTrys[1]
        reiksme = juost_1[2:]  # slicing
        reiksme = str(reiksme)
        print reiksme, ' juosta 1'

        colors = {'0': (0, 0, 0, 1), '1': (.4, .2, 0, 1), '2': (1, 0, 0, 1), '3': (1, .5, 0, 1), '4': (1, 1, 0, 1),
                  '5': (0, .6, 0, 1), '6': (0, 0, 1, 1), '7': (.4, 0, .4, 1), '8': (1, 1, 1, .5), '9': (1, 1, 1, 1)}
        for key, value in colors.iteritems():
            if key == reiksme:
                backgroundColor = value
        print colors
        print backgroundColor
        return backgroundColor

    def s2_color(*args):
        arglst = list()
        for arg in args:
            arglst.append(arg)
        tarp = arglst[1]
        visi = tarp.split()
        juost_2 = visi[2]
        reiksme = str(juost_2[2:])
        print reiksme, ' juosta 2'
        colors = {'0': (0, 0, 0, 1), '1': (.4, .2, 0, 1), '2': (1, 0, 0, 1), '3': (1, .5, 0, 1), '4': (1, 1, 0, 1),
                  '5': (0, .6, 0, 1), '6': (0, 0, 1, 1), '7': (.4, 0, .4, 1), '8': (1, 1, 1, .5), '9': (1, 1, 1, 1)}
        for key, value in colors.iteritems():
            if key == reiksme:
                backgroundColor = value
        print colors
        print backgroundColor
        return backgroundColor

    def s3_color(*args):
        arglst = list()
        for arg in args:
            arglst.append(arg)
        tarp = arglst[1]
        visi = tarp.split()
        juost_3 = visi[3]
        reiksme = str(juost_3[2:])
        print reiksme, ' juosta 2'
        colors = {'0': (0, 0, 0, 1), '1': (.4, .2, 0, 1), '2': (1, 0, 0, 1), '3': (1, .5, 0, 1), '4': (1, 1, 0, 1),
                  '5': (0, .6, 0, 1), '6': (0, 0, 1, 1), '7': (.4, 0, .4, 1), '8': (1, 1, 1, .5), '9': (1, 1, 1, 1)}
        for key, value in colors.iteritems():
            if key == reiksme:
                backgroundColor = value
        print colors
        print backgroundColor
        return backgroundColor

    def daugiklis_color(*args):
        arglst = list()
        for arg in args:
            arglst.append(arg)
        tarp = arglst[1]
        visiTrys = tarp.split()
        daugiklis = visiTrys[0]
        reiksme = str(daugiklis[1:])
        print reiksme, ' daugiklis'
        colors = {'1': (0, 0, 0, 1), '10': (.4, .2, 0, 1), '100': (1, 0, 0, 1), '1000': (1, .5, 0, 1),
                  '10000': (1, 1, 0, 1), '100000': (0, .6, 0, 1), '1000000': (0, 0, 1, 1),
                  '10000000': (.4, 0, .4, 1), '0.01': (1, 1, 1, .7), '0.1': (.84, .64, .125, 1)}
        for key, value in colors.iteritems():
            if key == reiksme:
                backgroundColor = value
        print colors
        print backgroundColor
        return backgroundColor

    # --------------------------------------3-tabas-------------------------------------

    def inp_testing(*args):  #funkcija naudojama 3 ir 4 tabu input tikrinimui
        lst = list()

        for arg in args:
            lst.append(arg)

        test = lst[1]
        try:
            x = float(test)
        except:
            if test is not float and test != '':
                popup = Popup(title='Eror:',
                              content=Label(text="Enter only numbers"),
                              size_hint=(None, None), size=(200, 200))
                popup.open()

    def volt_div(*args):
        lst = list()
        for arg in args:
            lst.append(arg)
        if lst[1] == '' or lst[2] == '' or lst[3] == '':
            rez = ''
        else:
            vin = float(lst[1])
            r1 = float(lst[2])
            r2 = float(lst[3])
            vout = round(((r2 / (r1 + r2)) * vin), 2)
            rez = str(vout) + "V"
        return rez

    # -------------------------------------------4-tabas--------------------------------------------

    def lm(*args):
        lst = list()
        for arg in args:
            lst.append(arg)
        if lst[1] == '' or lst[2] == '':
            rez1 = ''
        else:
            r1 = float(lst[1])
            r2 = float(lst[2])
            vout = round((1.25 * (1 + r1 / r2)), 2)
            rez1 = str(vout) + "V"
        return rez1


class ResistanceCalculatorApp(App):
    def build(self):
        return Tabbedpanel()


if __name__ == '__main__':
    ResistanceCalculatorApp().run()

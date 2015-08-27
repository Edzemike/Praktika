# coding=utf-8
__author__ = 'Edita'

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button
from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput

Builder.load_file("pagr.kv")  # Įkeliamas kivy tekstinis failas su programos išvaizdos aprašymais


class Tabbedpanel(TabbedPanel):  # šioje klasėje aprašomas visas programos veikimas
    '''def popupwindow1(self):
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

        return sk'''

    # ------------------------------- Pirmo tabo (skirtuko) funkcijos --Value-----------------------------

    def pirma_juostele(*args):  # funkcija paima  mygtuko  iš iššokančio lango(atidaromo paspaudus
        #  pirma varžo juostelę)  grąžinamus duomenis
        lst = list()  # sukuriamas tuščias sąrašas
        for arg in args:
            lst.append(arg)  # for cikle gauti argumentai sudedami i sąrašą
        n1 = str(lst[1])  # paimama reikalinga reikšmė, nulinis sąrašo elemntas yra adresas,
        #  skaičiavimui jis nebus reikalingas
        return n1  # grąžinama reikšmė bus panaudota pagr.kv faile

    def antra_juostele(*args):  # funkcija analogiška funkcijai pirma_juostele, iškyrus, duomenys imami iš
        # anrtos juostelės iššokancio lango mygtukų
        lst = list()
        for arg in args:
            lst.append(arg)
        n2 = str(lst[1])
        return n2

    def trecia_juostele(*args):  # funkcija analogiška funkcijai pirma_juostele, trečios juostelės duomenys
        lst = list()
        for arg in args:
            lst.append(arg)
        n3 = str(lst[1])
        return n3

    def ketvirta_juostele(*args):  # analogiška f-jai pirma_juostele, ketvirtos juostelės duomenys - daugiklis.
        lst = list()
        for arg in args:
            lst.append(arg)
        n4 = str(lst[1])
        return n4

    def rezultatas_4band(*args):  # f-ja apskaičiuoja varžo su 4 juost. varžą. Arg. persiųsti iš etiketės (id: tarpine)
        lst = list()
        for arg in args:
            lst.append(arg)
        skaicius = lst[1]  # iš arg. sąrašo paimama str tipo reikšmė ir priskiriama kintamąjam skaicius
        n1 = skaicius[0]   # iš kint. skaicius gaunamas pirmas rezultato skaičiavimo skaitmuo
        n2 = skaicius[1]   # 2-ras skaitmuo
        n4 = float(skaicius[2:])  # daugiklis
        n12 = int(n1 + n2)  # pirmas ir antras skaitmuo sujungiamas į vieną int tipo kintamąjį
        rez = n12 * n4  # apskaičiuojamas rezultatas
        if rez < 10:  # apsisaugoma, kad jei rezultatas < 10 į atsakymo laukelį būtų siunčiamas trupmeninis rezultatas
            rez = str(rez)  # etiketės (Label) priima tik str tipo kintamuosius
        else:
            rez = str(int(rez))  # jei rez dviženklis ar didesnis, rezultatas siunčiamas kaip sveikasis skaičius.
        return rez  # grąžinama reikmė bus išspausdinta etiketėje (id: resistance)

    def rezultatas_56band(*args):  # analogiška f-jai rezultatas_4band, tik rezultatas skaičiuojamas iš
        #  4 juostelių duomenų, ne trijų.
        lst = list()
        for arg in args:
            lst.append(arg)
        skaicius = lst[1]
        n1 = skaicius[0]
        n2 = skaicius[1]
        n3 = skaicius[2]
        n4 = float(skaicius[3:])
        n123 = int(n1 + n2 + n3)
        rez = n123 * n4
        if rez < 100:
            rez = str(rez)
        else:
            rez = str(int(rez))
        return rez

    # -------------------------------------- 2 skirtuko funkcijos---Colors------------------------------------

    def values_4band(*args):
        lst = list()
        for arg in args:
            lst.append(arg)  # paimamas TextInput tekstas (id: inp)

        if lst[1] != '':
            if lst[1].startswith('-'):  # tikrinama, ar vartotojas bando įvesti neigiamą reikšmę. jei taip,
                popup = Popup(title='Eror:',  # iššoksta pranešimas, kad varža negali būti neigiama.
                              content=Label(text="Resistance can not\nbe negative"),
                              size_hint=(None, None), size=(200, 200))  # nustatomas pranešimo lango dydis
                popup.open()
            sk = float(lst[1])  # gautas argumentas paverčiamas į float (svarbu, jei įvestas skaičius buvo float.
            if sk < 1:  # pagal skaičiaus dydį nustatomas jo daugiklis ir sk išskaidoms skaitmenimis
                daugiklis = 0.01
                sk = str(int(sk * 100))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 10:
                daugiklis = 0.1
                sk = str(int(sk * 10))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 100:
                daugiklis = 1
                sk = str(int(sk))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 1000:
                daugiklis = 10
                sk = str(int(sk / 10))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 10000:
                daugiklis = 100
                sk = str(int(sk / 100))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 100000:
                daugiklis = 1000
                sk = str(int(sk / 1000))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 1000000:
                daugiklis = 10000
                sk = str(int(sk / 10000))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 10000000:
                daugiklis = 100000
                sk = str(int(sk / 100000))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 100000000:
                daugiklis = 1000000
                sk = str(int(sk / 1000000))
                s1 = sk[0]
                s2 = sk[1]
            elif sk < 1000000000:
                daugiklis = 10000000
                sk = str(int(sk / 10000000))
                s1 = sk[0]
                s2 = sk[1]
            elif sk >= 1000000000:  # Jei skaičius viršija leistiną, iššoksta pranešimas "per didelis skaičius"
                popup = Popup(title='Eror:',
                              content=Label(text="Too large number"),
                              size_hint=(None, None), size=(200, 200))
                popup.open()
            ret_daugiklis = 'd' + str(daugiklis)  # suformuojami str tipo kintamieji su identifikacija pradžioje
            ret_s1 = 's1' + str(s1)
            ret_s2 = 's2' + str(s2)
            ret_list = list()
            ret_list.append(ret_daugiklis)  # kintamieji sudedami į sąrašą
            ret_list.append(ret_s1)
            ret_list.append(ret_s2)
            te = ' '.join(ret_list)  # sąrašas paverčiamas viena simbolių eilute
            return te  # simbolių eilutė grąžinama ir panaudojama už programos ribų esančioje tarpinėje
            #  etiketėje. id: lbl

    def values_5band(*args):  # analogiška f-jai values_4band, skiriasi naudojamų skaitmenų skaičius,
        # atsakymas formuojamas 4 juostelėms, ne trims
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

            if sk < 0.1:
                daugiklis = 0.01
                sk = str(int(sk * 100))
                s1 = 0,
                s2 = 0,
                s3 = sk[0]
            if sk < 1:
                daugiklis = 0.01
                sk = str(int(sk * 100))
                s1 = 0
                s2 = sk[0]
                s3 = sk[1]
            elif sk < 10:
                daugiklis = 0.01
                sk = str(int(sk * 100))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 100:
                daugiklis = 0.1
                sk = str(int(sk * 10))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 1000:
                daugiklis = 1
                sk = str(int(sk))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 10000:
                daugiklis = 10
                sk = str(int(sk / 10))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 100000:
                daugiklis = 100
                sk = str(int(sk / 100))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 1000000:
                daugiklis = 1000
                sk = str(int(sk / 1000))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 10000000:
                daugiklis = 10000
                sk = str(int(sk / 10000))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 100000000:
                daugiklis = 100000
                sk = str(int(sk / 100000))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 1000000000:
                daugiklis = 1000000
                sk = str(int(sk / 1000000))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk < 10000000000:
                daugiklis = 10000000
                sk = str(int(sk / 10000000))
                s1 = sk[0]
                s2 = sk[1]
                s3 = sk[2]
            elif sk >= 10000000000:  # leistina varža didesnė nei 4 juostelių kode.
                popup = Popup(title='Eror:',
                              content=Label(text="Too large number"),
                              size_hint=(None, None), size=(200, 200))
                popup.open()

            ret_daugiklis = 'd' + str(daugiklis)
            ret_s1 = 's1' + str(s1)
            ret_s2 = 's2' + str(s2)
            ret_s3 = 's3' + str(s3)
            ret_list = list()
            ret_list.append(ret_daugiklis)
            ret_list.append(ret_s1)
            ret_list.append(ret_s2)
            ret_list.append(ret_s3)
            te = ' '.join(ret_list)
            return te

    def s1_color(*args):  #surandama ir grąžinama pirmos juostelės spalva
        arglst = list()
        for arg in args:
            arglst.append(arg)
        tarp = arglst[1]  # paimama reikalinga reikšmė
        visi = tarp.split()  # suskaldo simbolių eilutę per tarpus ir sukuria sąrašą
        juost_1 = visi[1]   # imama reikšmė su identifikatoriumi s1 (sub1 sąrašo elementas)
        reiksme = juost_1[2:]  # slicing - iš str kintamojo paimamas tik skaitmuo
        reiksme = str(reiksme) # kontrolinis pavertimas į str tipo kintamąjį
        # sąraše kiekvienam skaitmeniui priskiriamas rgba spalvų kodas procentais
        colors = {'0': (0, 0, 0, 1), '1': (.4, .2, 0, 1), '2': (1, 0, 0, 1), '3': (1, .5, 0, 1), '4': (1, 1, 0, 1),
                  '5': (0, .6, 0, 1), '6': (0, 0, 1, 1), '7': (.4, 0, .4, 1), '8': (1, 1, 1, .5), '9': (1, 1, 1, 1)}
        for key, value in colors.iteritems():
            if key == reiksme:  # surandama skaičių atitinkanti spalva
                backgroundColor = value
        return backgroundColor  # grąžinamas spalvos kodas, bus panaudotas pirmai juostelei nuspalvinti

    def s2_color(*args):  # analogiška - s1_color
        arglst = list()
        for arg in args:
            arglst.append(arg)
        tarp = arglst[1]
        visi = tarp.split()
        juost_2 = visi[2]  # reikšmė su ident. s2 (sub2 elementas)
        reiksme = str(juost_2[2:])
        colors = {'0': (0, 0, 0, 1), '1': (.4, .2, 0, 1), '2': (1, 0, 0, 1), '3': (1, .5, 0, 1), '4': (1, 1, 0, 1),
                  '5': (0, .6, 0, 1), '6': (0, 0, 1, 1), '7': (.4, 0, .4, 1), '8': (1, 1, 1, .5), '9': (1, 1, 1, 1)}
        for key, value in colors.iteritems():
            if key == reiksme:
                backgroundColor = value
        return backgroundColor  # grąžinamas kodas, skirtas nuspalvinti antrą juostelę

    def s3_color(*args):  # analogiška  - s1_color
        arglst = list()
        for arg in args:
            arglst.append(arg)
        tarp = arglst[1]
        visi = tarp.split()
        juost_3 = visi[3]  # identif. s3, sub3 elementas
        reiksme = str(juost_3[2:])
        colors = {'0': (0, 0, 0, 1), '1': (.4, .2, 0, 1), '2': (1, 0, 0, 1), '3': (1, .5, 0, 1), '4': (1, 1, 0, 1),
                  '5': (0, .6, 0, 1), '6': (0, 0, 1, 1), '7': (.4, 0, .4, 1), '8': (1, 1, 1, .5), '9': (1, 1, 1, 1)}
        for key, value in colors.iteritems():
            if key == reiksme:
                backgroundColor = value
        return backgroundColor  # trečios juostelės spalva

    def daugiklis_color(*args):  # analogiška - s1_color, kitoks spalvų pasirinkimas
        arglst = list()
        for arg in args:
            arglst.append(arg)
        tarp = arglst[1]
        visiTrys = tarp.split()
        daugiklis = visiTrys[0]  # identifikatorius d, sub0 elementas
        reiksme = str(daugiklis[1:])  # kadangi identif. trumpesnis, imama nuo sub1 elemento
        colors = {'1': (0, 0, 0, 1), '10': (.4, .2, 0, 1), '100': (1, 0, 0, 1), '1000': (1, .5, 0, 1),
                  '10000': (1, 1, 0, 1), '100000': (0, .6, 0, 1), '1000000': (0, 0, 1, 1),
                  '10000000': (.4, 0, .4, 1), '0.01': (1, 1, 1, .7), '0.1': (.84, .64, .125, 1)}
        for key, value in colors.iteritems():
            if key == reiksme:
                backgroundColor = value
        return backgroundColor  # 4 juostelės spalva, 4-band-code atveju tai vizualiai trečia juostelė

    # --------------------------------------3-tabas--Voltage-Divider----------------------------------

    def inp_testing(*args):  # funkcija naudojama patikrinti 2, 3 ir 4 skirtukų įvestį.
        lst = list()

        for arg in args:
            lst.append(arg)

        test = lst[1]
        try:
            x = float(test)  # bandoma paversti į float tipo kintamąjį, siekiama išvengti raidinių reikšmių įvedimo
        except:
            if test is not float and test != '':  # jei pavertimas nepavyko ir įvedimo langelis nėra tuščias - popup
                popup = Popup(title='Eror:',
                              content=Label(text="Enter only numbers"),
                              size_hint=(None, None), size=(200, 200))
                popup.open()

    def volt_div(*args):  # siunčiama reikšmė jau buvo tikrinta prieš tai esančioje funkcijoje
        lst = list()
        for arg in args:
            lst.append(arg)
        if lst[1] == '' or lst[2] == '' or lst[3] == '':  # Jei nors vienas langelis tuščias,
            rez = ''  # rezultatas neišspausdinamas, t.y, į etiketę nusiunčia tuščia simbolių eilutė.
        else:
            vin = float(lst[1])  # visos įvestos reikšmės paverčiamos trupmeniniais skaičiais
            r1 = float(lst[2])
            r2 = float(lst[3])
            vout = round(((r2 / (r1 + r2)) * vin), 2)  # apskaičiuojama išvesties įtampa V out
            rez = str(vout) + "V"
        return rez  # rezultatas panaudojamas etiketėje prie schemos

    # -------------------------------------------4-tabas--LM-317-----------------------------------------

    def lm(*args):
        lst = list()
        for arg in args:
            lst.append(arg)
        if lst[1] == '' or lst[2] == '':  # Jei kuris nors langelis tuščias, rezultato etiketė irgi tuščia
            rez1 = ''
        else:
            r1 = float(lst[1])
            r2 = float(lst[2])
            vout = round((1.25 * (1 + r1 / r2)), 2)  # numatyta, kad įvesties įtampa 1,25V, apskaičiuojama išvesties.
            rez1 = str(vout) + "V"
        return rez1


class ResistanceCalculatorApp(App):  # klasė, sukurianti langą su TabbedPanel
    def build(self):
        return Tabbedpanel()


if __name__ == '__main__':
    ResistanceCalculatorApp().run()  # paleidžiama programa

#!/usr/bin/python
# Kivy: Multiple layouts with menu
# 28.05.2017, Nicolae Erast

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label

class MyLayout(BoxLayout):

    def __init__(self,**kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.showMenu()

    def showMenu(self,*args):
        self.clear_widgets()
        b1 = Button()
        b1.background_color = (1,0,0,1)
        b1.text = 'picture'
        b2 = Button()
        b1.background_color = (0,1,0,1)
        b2.text = 'about'
        b3 = Button()
        b3.background_color = (0,0,1,1)
        b3.text = 'exit'
        b1.bind(on_press = self.showPicture)
        b2.bind(on_press = self.showInfo)
        b3.bind(on_press = self.exitApp)
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)

    def showPicture(self,*args):
        self.clear_widgets()
        i1 = Image()
        i1.keep_ratio = True
        i1.source = 'simplekivy3.gif'
        self.add_widget(i1)
        b1 = Button()
        b1.size_hint_y = 0.1
        b1.background_color = (1,0,0,1)
        b1.text = '< -- Back'
        self.add_widget(b1)
        b1.bind(on_press = self.showMenu)
        
    def showInfo(self,*args):
        self.clear_widgets()
        l1 = Label()
        l1.text = 'Colourful informative label ;)'
        l1.color = (1,0,1,1)
        self.add_widget(l1)
        b1 = Button()
        b1.size_hint_y = 0.1
        b1.background_color = (1,0,0,1)
        b1.text = '< -- Back'
        self.add_widget(b1)
        b1.bind(on_press = self.showMenu)

    def exitApp(self,value):
        import os
        os._exit(0)
        
class Tema3(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    Tema3().run()

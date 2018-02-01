#!/usr/bin/python
# Kivy: Simple layout and on_press event
# 28.05.2017, Nicolae Erast

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyLayout(BoxLayout):

    def __init__(self,**kwargs):
        super(MyLayout, self).__init__(**kwargs)
        b1 = Button()
        b1.label = '<< Let\'s go >>'
        b1.background_color = (0,0,1,1)
        b2 = Button()
        b2.label = '<< Here i am >>'
        b2.background_color = (0,0,1,1)
        b1.bind(on_press = self.showLabel)
        b2.bind(on_press = self.showLabel)
        self.add_widget(b1)
        self.add_widget(b2)

    def showLabel(self,value):
        value.text = value.label
        
class Tema1(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    Tema1().run()

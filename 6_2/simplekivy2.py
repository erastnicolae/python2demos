#!/usr/bin/python
# Kivy: Changing layout properties
# 28.05.2017, Nicolae Erast

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyLayout(BoxLayout):

    def __init__(self,**kwargs):
        super(MyLayout, self).__init__(**kwargs)
        b1 = Button()
        b1.text = '<< Let\'s go >>'
        b1.background_color = (0,0,1,1)
        b2 = Button()
        b2.text = '<< Here i am >>'
        b2.background_color = (0,0,1,1)
        b1.bind(on_press = self.showLabel)
        b2.bind(on_press = self.showLabel)
        self.add_widget(b1)
        self.add_widget(b2)

    def showLabel(self,value):
        if value.text == '<< Let\'s go >>':
            value.color = (1,0,0,1)
        else:
            value.color = (0,1,0,1)
        
class Tema2(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    Tema2().run()

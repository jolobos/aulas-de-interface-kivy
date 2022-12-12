from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class incrementador(BoxLayout):
    pass

class Test(App):
    def build(self):
        return incrementador()




Test().run()
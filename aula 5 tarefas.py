from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Tarefas(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa))


class Test5(App):
    def build(self):
        return Tarefas(['fazer', 'buscar', 'o lokoh!!!'], orientation='horizontal')


Test5().run()

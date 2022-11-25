from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa, font_size=30, size_hint_y=None, height=150))


class Test6(App):
    def build(self):
        return Tarefas(['fazer', 'buscar', 'o lokoh!!!', 'kdksadjsadk', 'sdnsadj', 'asndsahas'])


Test6().run()

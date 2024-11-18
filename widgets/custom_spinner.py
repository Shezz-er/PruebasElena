from kivy.uix.spinner import Spinner
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty

class CustomSpinner(Spinner):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = DropDown()

        # Agregar opciones al DropDown
        for option in kwargs.get('values', []):
            btn = Button(text=option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            self.dropdown.add_widget(btn)

        self.dropdown.max_height = 150  # Ajusta la altura máxima del DropDown

        self.bind(on_release=self.open_dropdown)
    def open_dropdown(self, *args):
        self.dropdown.open(self)

    def select(self, text):
        self.text = text
        self.dropdown.dismiss()
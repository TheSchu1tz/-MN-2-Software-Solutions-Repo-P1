from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
import kivy.properties
from kivy.properties import ObjectProperty

class InputScreen(Screen):
    def selected(self, filename):
        print("Selected file: ", filename)

class InputLayout(Widget):
    filepath = ObjectProperty(None)
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
import kivy.properties
from kivy.properties import ObjectProperty

class InputScreen(Screen):
    pass

class InputLayout(Widget):
    filepath = ObjectProperty(None)
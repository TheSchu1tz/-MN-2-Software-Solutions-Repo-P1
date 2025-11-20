import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
kivy.require('2.3.1')

from components import balance_ship as BalanceShip

from screens.input.input_screen import InputScreen
from screens.ship.ship_screen import ShipScreen

class MainApp(App):
    def build(self):
        Builder.load_file("main.kv")
        Builder.load_file("screens/input/input_screen.kv")
        Builder.load_file("screens/ship/ship_screen.kv")

        sm = ScreenManager()
        sm.add_widget(InputScreen(name='input_screen'))
        sm.add_widget(ShipScreen(name='ship_screen'))

        return sm

def main():
    #filepath = input("Please provide the file to solve for: ")
    #file = BalanceShip.ReadFile(filepath)
    #manifest = BalanceShip.ParseFile(file)
    #startGrid = BalanceShip.CreateGrid(manifest)
    app = MainApp()
    app.run()

if __name__ == "__main__":
    main()
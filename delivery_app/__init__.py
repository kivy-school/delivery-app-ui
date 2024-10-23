from kivy_reloader.app import App

from delivery_app.screens.main_screen import MainScreen


class DeliveryApp(App):
    def build(self):
        return MainScreen()

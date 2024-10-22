from delivery_app.screens.main_screen import MainScreen
from kivy_reloader.app import App


class DeliveryApp(App):
    def build(self):
        return MainScreen()
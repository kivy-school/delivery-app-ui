from kivy.core.window import Window
from kivy_reloader.app import App

from delivery_app.screens.splash_screen import SplashScreen
from delivery_app.theme import load_theme

load_theme()

Window.size = (414, 896)


class DeliveryApp(App):
    def build(self):
        return SplashScreen()

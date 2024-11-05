import os

from kivy.uix.screenmanager import Screen
from kivy_reloader.utils import load_kv_path

splash_screen_kv = os.path.join(
    'delivery_app',
    'screens',
    'splash_screen',
    'splash_screen.kv',
)
load_kv_path(splash_screen_kv)


class SplashScreen(Screen):
    pass

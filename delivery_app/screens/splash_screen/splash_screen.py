import os

from kivy_reloader.utils import load_kv_path

from delivery_app.uix.debug_screen import DebugScreen

splash_screen_kv = os.path.join(
    'delivery_app',
    'screens',
    'splash_screen',
    'splash_screen.kv',
)
load_kv_path(splash_screen_kv)


class SplashScreen(DebugScreen):
    pass

import os

from kivy.properties import BooleanProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy_reloader.utils import load_kv_path

kv_path = os.path.join(
    'delivery_app',
    'uix',
    'debug_screen',
    'debug_screen.kv',
)

load_kv_path(kv_path)


class DebugScreen(Screen):
    source_opacity: float = NumericProperty(1)
    source: str = StringProperty()
    transparent: bool = BooleanProperty(False)
    debug: bool = BooleanProperty(True)

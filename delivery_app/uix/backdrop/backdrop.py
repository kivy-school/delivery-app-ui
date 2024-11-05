import os

from kivy.uix.boxlayout import BoxLayout
from kivy_reloader.utils import load_kv_path

backdrop_kv = os.path.join(
    'delivery_app',
    'uix',
    'backdrop',
    'backdrop.kv',
)

load_kv_path(backdrop_kv)


class Backdrop(BoxLayout):
    pass

import os

from kivy.metrics import dp
from kivy.properties import ColorProperty, ListProperty
from kivy.uix.button import Button
from kivy_reloader.utils import load_kv_path

button_primary_kv = os.path.join(
    'delivery_app',
    'uix',
    'button',
    'button_primary',
    'button_primary.kv',
)

load_kv_path(button_primary_kv)


class ButtonPrimary(Button):
    bg_color: list | tuple = ColorProperty()
    bg_color_down: list | tuple = ColorProperty()
    radius: list | tuple = ListProperty([dp(10)])

import os

from kivy.properties import ColorProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy_reloader.utils import load_kv_path

button_text_kv = os.path.join(
    'delivery_app',
    'uix',
    'button',
    'button_text',
    'button_text.kv',
)

load_kv_path(button_text_kv)


class ButtonText(ButtonBehavior, Label):
    color_normal: list | tuple = ColorProperty()
    color_down: list | tuple = ColorProperty()

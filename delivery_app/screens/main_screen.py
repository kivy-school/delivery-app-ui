import os

from kivy.uix.screenmanager import Screen

from kivy_reloader.utils import load_kv_path

main_screen_kv = os.path.join("delivery_app", "screens", "main_screen.kv")
load_kv_path(main_screen_kv)


class MainScreen(Screen):
    pass
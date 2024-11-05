import os

from kivy.lang import global_idmap


def load_font_styles():
    """
    Loads the application's font styles into Kivy's global_idmap.
    This makes the fonts accessible globally within KV files.
    """
    fonts_folder = os.path.join('delivery_app', 'assets', 'fonts')

    font_styles = {
        'sf_display_bold': f'{fonts_folder}/SF-Pro-Display-Bold.otf',
        'sf_display_medium': f'{fonts_folder}/SF-Pro-Display-Medium.otf',
        'sf_text_bold': f'{fonts_folder}/SF-Pro-Text-Bold.otf',
        'sf_text_medium': f'{fonts_folder}/SF-Pro-Text-Medium.otf',
        'sf_text_regular': f'{fonts_folder}/SF-Pro-Text-Regular.otf',
        'sf_text_semibold': f'{fonts_folder}/SF-Pro-Text-Semibold.otf',
    }

    # Update the global_idmap with the font styles
    global_idmap.update(font_styles)

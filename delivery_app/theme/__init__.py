from .colors import load_color_palette
from .fonts import load_font_styles


def load_theme():
    """
    Loads the application's theme by loading the color palette and font styles
    """
    load_color_palette()
    load_font_styles()

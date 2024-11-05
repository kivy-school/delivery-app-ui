from kivy.lang import global_idmap
from kivy.utils import rgba


def load_color_palette():
    """
    Loads the application's color palette into Kivy's global_idmap.
    This makes the colors accessible globally within KV files.
    """
    color_palette = {
        'text_primary': rgba('#2D0C57'),
        'text_secondary': rgba('#9586A8'),
        'selected_bg_violet': rgba('#E2CBFF'),
        'selected_violet': rgba('#7203FF'),
        'border': rgba('#D9D0E3'),
        'background': rgba('#F6F5F5'),
        'primary_button': rgba('#0BCE83'),
        'green': rgba('#CBF265'),
        'white': rgba('#FFFFFF'),
        'black': rgba('#000000'),
    }

    # Update the global_idmap with the color palette
    global_idmap.update(color_palette)

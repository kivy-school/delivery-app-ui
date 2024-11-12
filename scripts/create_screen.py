import os

app_name = 'delivery_app'


def snake_case(name: str) -> str:
    """
    Converts a string to snake_case
    """
    return name.strip().lower().replace(' ', '_')


def pascal_case(name: str) -> str:
    """
    Converts a string to PascalCase
    """
    return ''.join(word.capitalize() for word in name.strip().split())


def create_file_if_not_exists(file_path: str, content: str) -> None:
    """
    Creates a file in the given path with a specific content
    """
    if os.path.exists(file_path):
        print('The file already exists, ignoring...')
    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f'Created file {file_path}')


def create_dir_if_not_exists(dir_path: str) -> None:
    """
    Creates a directory if it doesn't already exists
    """
    if os.path.exists(dir_path):
        print(f'The directory {dir_path} already exists')
    else:
        os.makedirs(dir_path)
        print(f'Created directory {dir_path}')


def main():
    screen_name = input('Enter the screen name: \n> ')
    screen_snake = snake_case(screen_name)
    screen_pascal = pascal_case(screen_name)

    # the name of the folder
    target_dir = os.path.join(app_name, 'screens', screen_snake)

    # Step 1: Create the screen directory
    create_dir_if_not_exists(target_dir)

    # define file paths
    py_file = os.path.join(target_dir, f'{screen_snake}.py')
    kv_file = os.path.join(target_dir, f'{screen_snake}.kv')
    init_file = os.path.join(target_dir, '__init__.py')

    # content of the files
    py_content = f"""
import os

from kivy_reloader.utils import load_kv_path

from {app_name}.uix.debug_screen import DebugScreen

kv_path = os.path.join(
    '{app_name}',
    'screens',
    '{screen_snake}',
    '{screen_snake}.kv',
)
load_kv_path(kv_path)


class {screen_pascal}(DebugScreen):
    pass

""".strip()
    kv_content = f"""
<{screen_pascal}>:
    source: '{app_name}/assets/images/{screen_snake}.png'

    canvas.before:
        Color:
            rgba: background
        Rectangle:
            pos: self.pos
            size: self.size
""".strip()
    init_content = (
        f'from .{screen_snake} import {screen_pascal}  # noqa: F401\n'
    )

    # Step 2: we create the python file
    create_file_if_not_exists(py_file, py_content)

    # Step 3: we create the kv file
    create_file_if_not_exists(kv_file, kv_content)

    # Step 4: we create the __init__.py file
    create_file_if_not_exists(init_file, init_content)


if __name__ == '__main__':
    main()

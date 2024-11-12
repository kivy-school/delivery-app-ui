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
    component_name = input('Enter the component name: \n> ')
    component_snake = snake_case(component_name)
    component_pascal = pascal_case(component_name)

    # the name of the folder
    target_dir = os.path.join(app_name, 'uix', component_snake)

    # Step 1: Create the component directory
    create_dir_if_not_exists(target_dir)

    # define file paths
    py_file = os.path.join(target_dir, f'{component_snake}.py')
    kv_file = os.path.join(target_dir, f'{component_snake}.kv')
    init_file = os.path.join(target_dir, '__init__.py')

    # content of the files
    py_content = f"""
import os

from kivy.uix.boxlayout import BoxLayout
from kivy_reloader.utils import load_kv_path

kv_path = os.path.join(
    '{app_name}',
    'uix',
    '{component_snake}',
    '{component_snake}.kv',
)
load_kv_path(kv_path)


class {component_pascal}(BoxLayout):
    pass

""".strip()
    kv_content = f'<{component_pascal}>:'

    init_content = (
        f'from .{component_snake} import {component_pascal}  # noqa: F401\n'
    )

    # Step 2: we create the python file
    create_file_if_not_exists(py_file, py_content)

    # Step 3: we create the kv file
    create_file_if_not_exists(kv_file, kv_content)

    # Step 4: we create the __init__.py file
    create_file_if_not_exists(init_file, init_content)


if __name__ == '__main__':
    main()

"""Ventana para registrar a un usuario."""
import os

import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import input_widget, exitbar_widget, separator_widget, header_widget


# path del icon que usa esta ventana
REGISTER_ICON = os.path.join(
    'resources', 
    'icons', 
    'outline_account_circle_black_48dp.png'
)


def build():
    """Construye y retorna la ventana de registro."""
    header = header_widget.build(
        REGISTER_ICON, 
        'REGISTRO', 
        'Su usuario no existe\nComplete los campos para registrarse'
    )

    return sg.Window(
        title='MemPy',
        layout=[
            [exitbar_widget.build(colors.PRIMARY_DARK)],
            [header],
            [input_widget.build('- GÉNERO -', '-GENERO-')],
            [input_widget.build('- EDAD -', '-EDAD-')],
            [sg.Button('REGISTRARSE', k='-REGISTRARSE-', bind_return_key=True)],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 1)],
            [sg.Button('VOLVER ATRÁS', k='-BACK-')],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 1)]
        ],
        keep_on_top=True,
        no_titlebar=True,
        element_justification='c',
        background_color=colors.BACKGROUND,
        finalize=True
    )
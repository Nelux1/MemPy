"""Ventana que se muestra al iniciar MemPy. Login del usuario."""
import os

import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import input_widget, exitbar_widget, separator_widget, header_widget


# path del icon que usa esta ventana
LOGIN_ICON = os.path.join(
    'resources', 
    'icons', 
    'outline_extension_black_48dp.png'
)


def build():
    """Construye y retorna la ventana de login."""
    header = header_widget.build(
        img_path=LOGIN_ICON, 
        title='MEMPY', 
        subtitle='el clásico juego de la memoria'
    )

    login_bttn = sg.Button(
        button_text='INGRESAR',
        key='-LOGIN-', 
        border_width=0, 
        font=('courier', 10), 
        size=(30, 2), 
        button_color=(colors.WHITE, colors.SECONDARY), 
        bind_return_key=True
    )

    footer = sg.Text(
        text='combine letras, números, puntos y guiones bajos\nmínimo 3 caracteres', 
        justification='center', 
        font=('courier', '10'), 
        background_color=colors.PRIMARY_LIGHT, 
        text_color=colors.BLACK
    )

    return sg.Window(
        title='MemPy', 
        layout=[
            [exitbar_widget.build(colors.PRIMARY)],
            [header],
            [input_widget.build('- NOMBRE DE USUARIO -', '-USERNAME-')],
            [login_bttn],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
            [footer],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 1)]
        ], 
        keep_on_top=True, 
        no_titlebar=True,
        background_color=colors.PRIMARY_LIGHT,
        element_justification='c',
        finalize=True
    )
"""Ventana que lleva a los diferentes tipos de configuraciones.

    Interactua con las ventanas en windows/config_windows
"""
import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import exitbar_widget, separator_widget, option_widget


def build():
    """Construye y retorna la ventana de inicio de configuraciones."""
    title = sg.Text(
        text='Configuraciones',
        font=('times', 30, 'bold'),
        background_color=colors.PRIMARY_LIGHT,
        text_color=colors.BLACK,
        size=(25, 1),
        justification='c'
    )

    level_select = option_widget.build(
        'Elegir nivel a configurar',
       '-NIVEL-',
        [1, 2, 3],
        1
    )

    return sg.Window(
        title='',
        layout=[
            [exitbar_widget.build(colors.PRIMARY_LIGHT)],
            [title],
            [separator_widget.estilo2(colors.PRIMARY_LIGHT, colors.BLACK)],
            [level_select],
            [option_button('Mensajes', '-MENSAJES-')],
            [option_button('Partida', '-PARTIDA-')],
            [option_button('Estilos', '-ESTILO-')],
            [option_button('Volver', '-BACK-')],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
        ],
        no_titlebar=True,
        keep_on_top=True,
        element_justification='c',
        background_color=colors.PRIMARY_LIGHT,
        finalize=True
    )


def option_button(text, key):
    """Botones utilizados unicamente por esta ventana."""
    return sg.Button(
        button_text=text,
        key=key,
        font=('courier', 16),
        button_color=(colors.WHITE, colors.BLACK),
        mouseover_colors=(colors.BLACK, colors.PRIMARY),
        pad=(0, 10),
    )
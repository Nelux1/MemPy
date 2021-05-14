"""Ventana básica para mostrar y manejar configuraciones.

    Es útil porque las ventanas de configuración tienen
    el mismo estilo. Se busca extraer lo común.
"""
import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import exitbar_widget,separator_widget


def build(title, opciones):
    """Crea una ventana de configuraciones.

        Parametros
        ----------
            title : str
                El titulo de la ventana
            opciones : sg.Column
                Un contenedor de las opciones que se desea presentar.
    """
    title = sg.Text(
        text='Configuración de\nmensajes',
        justification='c',
        background_color=colors.PRIMARY_LIGHT,
        text_color=colors.BLACK,
        font=('times', 30, 'bold'),
        size=(25, None)
    )

    guardar = sg.Button(
        button_text='Guardar',
        key='-GUARDAR-',
        font=('courier', 13),
        size=(25, 3),
        pad=(20, 0)
    )

    cancelar = sg.Button(
        button_text='Cancelar',
        key='-CANCELAR-',
        font=('courier', 13),
        size=(25, 3)
    )

    return sg.Window(
        title='',
        layout=[
            [exitbar_widget.build(colors.PRIMARY_LIGHT)],
            [title],
            [separator_widget.estilo2(colors.PRIMARY_LIGHT, colors.BLACK)],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
            [opciones],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
            [guardar, cancelar],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
        ],
        no_titlebar=True,
        keep_on_top=True,
        grab_anywhere=True,
        background_color=colors.PRIMARY_LIGHT,
        element_justification='c',
        finalize=True
    )
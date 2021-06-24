"""Ventana que permite jugar y moverse por diferentes ventanas."""
import os

import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import exitbar_widget, separator_widget


# path del icon que usa esta ventana
HOME_ICON = os.path.join(
    'resources', 
    'icons', 
    'oculta.png'
)


def build():
    """Construye y retorna la ventana principal del juego."""
    logo = sg.Image(
        filename=HOME_ICON, 
        background_color=colors.BACKGROUND
    )

    title = sg.Text(
        text='INICIO', 
        background_color=colors.BACKGROUND, 
        size=(20, None),
        justification='c', 
        font=('Courier', 50, ''), 
        text_color=colors.BLACK
    )

    # fila de botones
    buttons = sg.Column(
        layout=[
            [
                button('JUGAR', '-JUGAR-'), 
                button('PUNTAJES', '-PUNTAJES-'), 
                button('ESTADíSTICAS', '-ESTADISTICAS-'), 
                button('CONFIGURACIÓN', '-CONFIG-')
            ]
        ], 
        background_color=colors.BACKGROUND,
        expand_x=True, 
        element_justification='c'
    )

    return sg.Window(
        title='', 
        layout= [
            [exitbar_widget.build(colors.BACKGROUND)],
            [separator_widget.estilo1(colors.BACKGROUND, colors.BLACK, 100)],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 2)],
            [logo],
            [title],
            [separator_widget.estilo2(colors.BACKGROUND, colors.BLACK)],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 2)],
            [buttons],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 2)],
            [separator_widget.estilo1(colors.BACKGROUND, colors.BLACK, 100)],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 2)]
        ], 
        no_titlebar=True,
        keep_on_top=True,
        background_color=colors.BACKGROUND,
        element_justification='c',
        finalize=True
    )


def button(text, key):
    """Los botones utilizados unicamente por esta ventana."""
    return sg.Button(
        button_text=text, 
        border_width=0, 
        key=key, 
        font=('courier', 10), 
        size=(18, 2), 
        button_color=(colors.WHITE, colors.BLACK),
        pad=((10, 10), (0, 0))
    )
"""Ventana que permite jugar y moverse por diferentes ventanas."""
import os

import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import exitbar_widget, separator_widget

HOME_ICON = os.path.join('resources', 'icons', 'outline_home_black_48dp.png')


def build():
    # agrega espacio arriba del logo
    top_logo_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)

    logo = sg.Image(
        filename=HOME_ICON, 
        background_color=colors.PRIMARY_LIGHT
    )

    title = sg.Text(
        text='INICIO', 
        background_color=colors.PRIMARY_LIGHT, 
        size=(20, None), # define el ancho de la ventana
        justification='c', 
        font=('Courier', 50, ''), 
        text_color=colors.BLACK
    )

    # agrega espacio debajo del titulo
    bottom_title_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)

    # fila de botones
    buttons = sg.Column(
        layout=[
            [button('JUGAR', '-JUGAR-'), button('PUNTAJES', '-PUNTAJES-'), button('ESTADíSTICAS', '-STATS-'), button('CONFIGURACIÓN', '-CONFIG-')]
        ], 
        background_color=colors.PRIMARY_LIGHT,
        expand_x=True, 
        element_justification='c'
    )

    # agrega espacio debajo de los botones
    bottom_bttns_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)

    # agrega espacio debajo del separador 
    bottom_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)

    layout = [
        [exitbar_widget.build(colors.PRIMARY_LIGHT)],
        [separator_widget.separator1(colors.PRIMARY_LIGHT, colors.BLACK, 100)],
        [top_logo_sep],
        [logo],
        [title],
        [separator_widget.separator2(colors.PRIMARY_LIGHT, colors.BLACK)],
        [bottom_title_sep],
        [buttons],
        [bottom_bttns_sep],
        [separator_widget.separator1(colors.PRIMARY_LIGHT, colors.BLACK, 100)],
        [bottom_sep]
    ]
    
    window = sg.Window(
        '', 
        layout=layout, 
        no_titlebar=True,
        keep_on_top=True,
        grab_anywhere=True,
        background_color=colors.PRIMARY_LIGHT,
        element_justification='c',
        finalize=True
    )
    
    return window


def button(text, key):
    return sg.Button(button_text=text, border_width=0, key=key, font=('courier', 10), size=(18, 2), button_color=(colors.WHITE, colors.SECONDARY), pad=((10, 10), (0, 0)))
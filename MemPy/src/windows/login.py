"""Ventana que se muestra al iniciar MemPy. Login del usuario."""
import os

import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import input_widget, exitbar_widget, separator_widget


LOGIN_ICON = os.path.join('resources', 'icons', 'outline_extension_black_48dp.png')


def build():
    logo = sg.Image(
        filename=LOGIN_ICON, 
        background_color=colors.PRIMARY
    )

    title = sg.Text(
        text='MEMPY',
        background_color=colors.PRIMARY,
        size=(13, None), # da el ancho a la ventana
        justification='c', 
        font=('Courier', 50, ''),
        text_color=colors.BLACK
    )

    subtitle = sg.Text(
        text='el clásico juego de la memoria', 
        background_color=colors.PRIMARY, 
        font=('Courier', 15), 
        text_color=colors.BLACK, 
        pad=((0, 0), (20, 0))
    )

    # agrega espacio debajo del subitulo
    bottom_subtitle_sep = separator_widget.invisible_horizontal(colors.PRIMARY, 2)

    header = sg.Column(
        layout=[
            [logo],
            [title],
            [separator_widget.separator2(colors.PRIMARY, colors.BLACK)],
            [subtitle],
            [bottom_subtitle_sep]
        ], 
        background_color=colors.PRIMARY, 
        expand_x=True, 
        element_justification='c'
    )

    # agrega espacio arriba del campo de input
    top_input_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)

    user_input = input_widget.build(
        '- NOMBRE DE USUARIO -',
        '-USERNAME-', 
        colors.PRIMARY_LIGHT, 
        colors.BLACK, 
        True
    )

    # agrega espacio arriba del boton de ingresar
    top_loginbttn_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)

    login_bttn = sg.Button(
        button_text='INGRESAR', 
        border_width=0, 
        key='-LOGIN-', 
        font=('courier', 10), 
        size=(30, 2), 
        button_color=(colors.WHITE, colors.SECONDARY), 
        bind_return_key=True
    )

    # agrega espacio debajo del boton de ingresar
    bottom_loginbttn_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)

    footer = sg.Text(
        text='combine letras, números, puntos y guiones bajos\nmínimo 3 caracteres', 
        justification='center', 
        font=('courier', '10'), 
        background_color=colors.PRIMARY_LIGHT, 
        text_color=colors.BLACK
    )

    # agrega espacio debajo del footer
    bottom_footer_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 1)

    layout = [
        [exitbar_widget.build(colors.PRIMARY)],
        [header],
        [top_input_sep],
        [user_input],
        [top_loginbttn_sep],
        [login_bttn],
        [bottom_loginbttn_sep],
        [footer],
        [bottom_footer_sep]
    ]

    # fijamos el size de la ventana con desde el title,
    # porque hacerlo desde el obj window con size=() genera problemas
    # a la hora de usar distintas resoluciones en distintas pcs.
    window = sg.Window(
        title='', 
        layout=layout, 
        keep_on_top=True, 
        no_titlebar=True, 
        grab_anywhere=True,
        background_color=colors.PRIMARY_LIGHT,
        element_justification='c'
    )
    
    return window
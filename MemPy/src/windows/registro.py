"""Ventana para registrar a un usuario."""
import os

import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import input_widget, exitbar_widget, separator_widget


# path del icon que usa esta ventana
REGISTER_ICON = os.path.join('resources', 'icons', 'outline_account_circle_black_48dp.png')


# opciones globales de la ventana
sg.set_options(
    button_element_size=(30, 2),
    button_color=(colors.WHITE, colors.SECONDARY),
    font=('courier', 10),
    border_width=0
)


def build():
    """Construye y retorna la ventana de registro."""
    logo = sg.Image(
        filename=REGISTER_ICON, 
        background_color=colors.PRIMARY
    )

    title = sg.Text(
        text='REGISTRO', 
        background_color=colors.PRIMARY, 
        justification='c',
        size=(13, None), # define el ancho de la ventana
        font=('Courier', 50, ''), 
        text_color=colors.BLACK
    )

    subtitle = sg.Text(
        text='Su usuario no existe\nComplete los campos para registrarse', 
        background_color=colors.PRIMARY, 
        font=('Courier', 13), 
        text_color=colors.BLACK,
        justification='c',
        pad=((0, 0), (20, 0))
    )

    # agrega espacio debajo del titulo
    bottom_title_sep = separator_widget.invisible_horizontal(colors.PRIMARY, 2)
    
    header = sg.Column(
        layout=[
            [logo],
            [title],
            [separator_widget.separator2(colors.PRIMARY, colors.BLACK)],
            [subtitle],
            [bottom_title_sep]
        ], 
        background_color=colors.PRIMARY, 
        expand_x=True, 
        element_justification='c'
    )

    # agrega espacio arriba del input de genero
    top_gender_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)

    gender_input = input_widget.build(
        '- GÉNERO -', 
        '-GENERO-', 
        colors.PRIMARY_LIGHT, 
        colors.BLACK, 
        True
    )

    # agrega espacio arriba del input de edad
    top_age_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 1)

    age_input = input_widget.build(
        '- EDAD -', 
        '-EDAD-', 
        colors.PRIMARY_LIGHT, 
        colors.BLACK, 
        False
    )
    
    # agrega espacio arriba del boton de registrarse
    top_regbttn_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)

    register_bttn =  sg.Button(
        button_text='REGISTRARSE', 
        key='-REGISTRARSE-', 
        bind_return_key=True, 
    )

    # agrega espacio arriba del boton de volver atras
    top_backbttn_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 1)

    back_bttn =  sg.Button(
        button_text='VOLVER ATRÁS', 
        key='-BACK-',
    )

    # agrega espacio debajo del boton de volver atras
    bottom_backbttn_sep = separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 1)


    layout = [
        [exitbar_widget.build(colors.PRIMARY)],
        [header],
        [top_gender_sep],
        [gender_input],
        [top_age_sep],
        [age_input],
        [top_regbttn_sep],
        [register_bttn],
        [top_backbttn_sep],
        [back_bttn],
        [bottom_backbttn_sep]
    ]
    
    # fijamos el size de la ventana con desde el title,
    # porque hacerlo desde el obj window con size=() genera problemas
    # a la hora de usar distintas resoluciones en distintas pcs.
    window = sg.Window(
        '', 
        layout=layout,
        keep_on_top=True,
        no_titlebar=True, 
        grab_anywhere=True,
        element_justification='c',
        background_color=colors.PRIMARY_LIGHT,
        finalize=True
    )
    
    return window
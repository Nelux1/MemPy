import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import option_widget, separator_widget, exitbar_widget


def build():
    title = sg.Text(
        text='Configuración de\nmensajes',
        justification='c',
        background_color=colors.PRIMARY_LIGHT,
        text_color=colors.BLACK,
        font=('times', 30, 'bold'),
        size=(25, None)
    )

    tema = option_widget.build(
        'Tema', 
        '-TEMA-', 
        ['Claro', 'Oscuro'], 
        'Claro'
    )

    guardar = sg.Button(
        button_text='Guardar',
        key='-GUARDAR-',
        font=('courier', 13),
        size=(25, 3)
    )

    mid_sep = sg.Text(background_color=colors.PRIMARY_LIGHT, size=(1, None))

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
            [separator_widget.separator2(colors.PRIMARY_LIGHT, colors.BLACK)],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
            [tema],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
            [guardar, mid_sep, cancelar],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
        ],
        background_color=colors.PRIMARY_LIGHT,
        no_titlebar=True,
        keep_on_top=True,
        grab_anywhere=True,
        element_justification='c'
    )
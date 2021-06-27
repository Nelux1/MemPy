"""Un popup para mostrar mensajes cortos."""
import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import separator_widget


def build(mensaje):
    
    return sg.Window(
        title='MemPy',
        layout=[
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 1)],
            [sg.Text(
                text=mensaje, 
                background_color=colors.BACKGROUND, 
                text_color=colors.BLACK, 
                font=('times', 20, 'bold'),
                size=(20, None),
                justification='c'
                )
            ],
            [separator_widget.estilo2(colors.BACKGROUND, colors.BLACK)],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 1)],
            [sg.Button(button_text='ACEPTAR', button_color=(colors.WHITE, colors.PRIMARY_LIGHT))],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 1)]
        ],
        element_justification='c',
        no_titlebar=True,
        keep_on_top=True,
        grab_anywhere=True,
        finalize=True,
        background_color=colors.BACKGROUND
    )
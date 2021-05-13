"""Punto de ejecución de las ventanas."""
import PySimpleGUI as sg

from src.components import login
# from src.components import config
from src.windows import colors


def run():
    # global settings
    sg.theme('dark teal 11')


    sg.set_options(
        auto_size_buttons=False,
        margins=(0, 0),
        element_padding=(0, 0),
        button_element_size=(30, 2),
        button_color=(colors.WHITE, colors.SECONDARY),
        font=('courier', 10),
        border_width=0
    )
    # config.start()
    login.start()
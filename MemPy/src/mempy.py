"""Punto de ejecución de las ventanas."""
# from src.components import login

# def run():
#     login.start()

import PySimpleGUI as sg
from src.windows import login, registro, inicio


# global settings
sg.set_options(
    auto_size_buttons=False,
    margins=(0, 0),
    element_padding=(0, 0)
)


login.build().read(close=True)
registro.build().read(close=True)
inicio.build().read(close=True)
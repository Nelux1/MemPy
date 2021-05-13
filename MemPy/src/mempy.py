"""Punto de ejecución de las ventanas."""
import PySimpleGUI as sg

from src.components import login


def run():
    # global settings
    sg.set_options(
        auto_size_buttons=False,
        margins=(0, 0),
        element_padding=(0, 0)
    )

    login.start()
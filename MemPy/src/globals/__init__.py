"""Este paquete contiene información de estilo.

    Estos estilos o:
        - Se comparten entre varias ventanas.
        - Se desea que no queden "esparcidos" por el código y sean
        fáciles de encontrar y actualizar.
"""

import PySimpleGUI as sg

import src.globals.colors as colors
import src.globals.fonts as fonts


# global settings
sg.set_options(
    font=fonts.FONT,
    auto_size_buttons=False,
    margins=(0, 0),
    element_padding=(0, 0)
)
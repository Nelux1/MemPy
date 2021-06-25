import os
from os.path import sep

import PySimpleGUI as sg

from src.windows.widgets import separator_widget


def build(color):
    """Retorna una barra con una X de salida a la derecha. 

        Parámetros
        ----------
            color : str
                valor hexa para el color de fondo de la barra
    
        Return
        ------
            bar : sg.Column
    """
    abandono_bttn = sg.Button(
        key='-ABANDONAR-',
        tooltip='Abandonar',
        pad=(10,0), # separación del borde derecho
        border_width=0,
        button_color=(color, color),
        image_filename=os.path.join('resources', 'icons', 'ab.png'),
        image_size=(25, 25),
        image_subsample=4
    )
    
    return sg.Column(
        layout=[
            [separator_widget.invisible_horizontal(color, 1)],
            [abandono_bttn],
            [separator_widget.invisible_horizontal(color, 1)]
        ], 
        background_color=color, 
        expand_x=True, 
        element_justification='r',
        grab=True
    )
"""Inputs personalizados, utilizados en las ventanas login.py y registro.py"""
import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import separator_widget


LABEL_FONT = ('Courier', 13)
INPUT_FONT = ('Courier', 20)
INPUT_UNDERLINE = ('Courier', 1, 'underline')


def build(label_text, key,):
    """Retorna una barra de input con estilo pseudo moderno.
    
    
        Parametros
        ----------
            label : str
                texto indicador arriba del input
            key : str
                clave que va a tener el objeto input
            focus : boolean
                si el input va a tener focus o no

            el resto son parámetros de personalización.
    """

    # texto indicador arriba del campo de input
    label = sg.Text(
        text=label_text, 
        background_color=colors.BACKGROUND, 
        text_color=colors.BLACK, 
        font=LABEL_FONT
    )

    # el objeto input
    input_elem = sg.Input(
        key=key, 
        size=(15, None), 
        border_width=0, 
        background_color=colors.BACKGROUND,
        text_color=colors.BLACK, 
        font=INPUT_FONT, 
        justification='c'
    )

    # imaginar que es parte del obj input también
    input_underline = sg.Text(
        '_'*248,
        text_color=colors.BLACK,
        background_color=colors.BACKGROUND, 
        font=INPUT_UNDERLINE
    )
        
    return sg.Column(
        layout=[
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 2)],
            [label], 
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 1)], 
            [input_elem], 
            [input_underline],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 2)]
        ], 
        background_color=colors.BACKGROUND,
        element_justification='c'
    )
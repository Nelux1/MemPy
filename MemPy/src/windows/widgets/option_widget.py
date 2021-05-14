""""Elementos que permiten elegir entre varias opciones.

    Utilizados en las ventanas de configuración.
"""
import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import separator_widget


def build(text, key, values, default):
    """Elemento de selección con un label."""
    label = sg.Text(
        text=text,
        text_color=colors.BLACK,
        font=('times', 18),
        background_color=colors.PRIMARY_LIGHT
    )
    
    return sg.Column(
        layout=[
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 1)],
            [label],
            [custom_combo(values, default, key)],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 1)]
        ],
        element_justification='c',
        background_color=colors.PRIMARY_LIGHT
    )
    

def custom_combo(values, default, key):
    """Combo únicamente utilizado por este widget."""
    return sg.Combo(
        key=key,
        values=values,
        default_value=default,
        background_color=colors.WHITE,
        font=('courier', 15),
        auto_size_text=False,
        size=(35, None),
        text_color=colors.BLACK,
        readonly=True
    )


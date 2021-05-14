"""Header utilizado en las ventanas login.py y registro.py"""
import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import separator_widget


def build(img_path, title, subtitle):
    """Retorna sg.Column con logo, titulo y subtitulo."""
    logo = sg.Image(
        filename=img_path, 
        background_color=colors.PRIMARY
    )

    title = sg.Text(
        text=title, 
        size=(13, None),
        justification='c',
        text_color=colors.BLACK,
        font=('Courier', 50, ''), 
        background_color=colors.PRIMARY,
    )

    subtitle = sg.Text(
        text=subtitle, 
        justification='c',
        font=('Courier', 13), 
        pad=((0, 0), (20, 0)), # separación del título
        text_color=colors.BLACK,
        background_color=colors.PRIMARY, 
    )

    return sg.Column(
        layout=[
            [logo],
            [title],
            [separator_widget.estilo2(colors.PRIMARY, colors.BLACK)],
            [subtitle],
            [separator_widget.invisible_horizontal(colors.PRIMARY, 2)]
        ], 
        background_color=colors.PRIMARY,
        expand_x=True,
        element_justification='c'
    )
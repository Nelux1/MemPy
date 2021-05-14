"""Separadores utilizados para agregar espacio entre elementos de psg."""
import PySimpleGUI as sg


def estilo1(background_color, text_color, width):
    """Crea un separador con signos de igual."""
    return sg.Text('═'*width, text_color=text_color, background_color=background_color)


def estilo2(background_color, text_color):
    """Separador con estilo _ . _"""
    return sg.Text('____________ . ____________', background_color=background_color, text_color=text_color)


def invisible_horizontal(background_color, height):
    """Separador con el tamaño dado."""
    return sg.Text('', size=(None, height), background_color=background_color)
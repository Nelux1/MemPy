"""Una de las ventanas abiertas por el menu config.py"""
import PySimpleGUI as sg

from src.windows.config_windows import base
from src.windows.widgets import option_widget


def build():
    """Construye y retorna la ventana de configuraciones de estilo."""
    return base.build(
        title='Configuración de\nmensajes',
        opciones=option_widget.build(
            text='Tema', 
            key='-TEMA-', 
            values=[
                'Claro', 
                'Oscuro'
            ], 
            default='Claro'
        )
    )
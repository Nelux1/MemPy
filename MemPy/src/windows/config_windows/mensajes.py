"""Una de las ventanas abiertas por el menu config.py"""
import PySimpleGUI as sg

from src.windows import colors
from src.windows.config_windows import base
from src.windows.widgets import option_widget


def build():
    """Construye y retorna la ventana de configuraciones de mensajes."""
    victoria = option_widget.build(
        text='Mensaje de Victoria', 
        key='-WIN_MESSAGE-',
        values=[
            '¡Ganaste!', 
            '¡Victoria!', 
            '¡No estuvo mal!', 
            '¡Muy bien!', 
            '¡Lo lograste!'
        ],
        default='¡Ganaste!',
    )

    derrota = option_widget.build(
        text='Mensaje de Derrota',
        key='-LOSS_MESSAGE-',
        values=[
            '¡Perdiste!', 
            '¡Derrota!', 
            'Casi... pero ¡perdiste!', 
            '¡Mejor suerte para la próxima!', 
            '¡A seguir intentando!'
        ],
        default='¡Perdiste!',
    )

    restante = option_widget.build(
        text='Mensaje del Tiempo Restante',
        key='-TIMELEFT_MESSAGE-',
        values=[
            '¡Quedan {} segundos!', 
            'Tiempo restante: {}', 
            'Faltan {} segundos para terminar', 
            '¡Mira el tiempo que perdiste! {}'
        ],
        default='¡Quedan {} segundos!',
    )

    return base.build(
        title='Configuración de\nmensajes',
        opciones= sg.Column(
            layout=[
                [victoria],
                [derrota],
                [restante]
            ],
            background_color=colors.BACKGROUND,
            justification='c'
        )
    )
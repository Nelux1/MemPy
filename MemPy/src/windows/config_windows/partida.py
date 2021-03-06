"""Una de las ventanas abiertas por el menu config.py"""
import PySimpleGUI as sg

from src.windows import colors
from src.windows.config_windows import base
from src.windows.widgets import option_widget


def build():
    casillas = option_widget.build(
        text='Tamaño del Tablero',
        key='-CASILLAS-',
        values=[
            '4x2', 
            '4x3', 
            '4x4'
        ],
        default='4x2'
    )

    coincidencias = option_widget.build(
        text='Coincidencias a buscar',
        key='-COINCIDENCIAS-',
        values=['2','3 (proximamente)'],
        default='2'
    )

    tipo_elementos = option_widget.build(
        text='Tipo de Elementos en Casillas',
        key='-ELEMENTOS-',
        values=[
            'Palabras', 
            'Imagenes'
        ],
        default='Palabras'
    )

    tiempo = option_widget.build(
        text='Duración de la Partida',
        key='-TIEMPO_MIN-',
        values=[
            '1 minuto', 
            '1:30 minutos', 
            '2 minutos', 
            '3 minutos', 
            '5 minutos'
        ],
        default='2 minutos'
    )

    pistas = sg.Checkbox(
        text='Pistas',
        key= '-PISTAS-',
        background_color=colors.BACKGROUND,
        font=('courier', 20),
        text_color=colors.BLACK
    )

    return base.build(
        title='Configuración de\npartida',
        opciones=sg.Column(
            layout=[
                [casillas],
                [coincidencias],
                [tipo_elementos],
                [tiempo],
                [pistas]
            ],
            background_color=colors.BACKGROUND
        )
    )
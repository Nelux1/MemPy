from src.components import config
import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import separator_widget, exitbar_widget, option_widget


def build():
    title = sg.Text(
        text='Configuración de\npartida',
        justification='c',
        background_color=colors.PRIMARY_LIGHT,
        text_color=colors.BLACK,
        font=('times', 30, 'bold'),
        size=(25, None)
    )

    casillas = option_widget.build(
        'Tamaño del Tablero',
        '-CASILLAS-',
        ['8x8', '16x16', '20x20'],
        '8x8'
    )

    coincidencias = option_widget.build(
        'Coincidencias a buscar',
        '-COINCIDENCIAS-',
        [2, 3, 4, 5],
        2
    )

    tipo_elementos = option_widget.build(
        'Tipo de Elementos en Casillas',
        '-ELEMENTOS-',
        ['Palabras', 'Imágenes', 'Palabras e Imágenes'],
        'Palabras'
    )

    tiempo = option_widget.build(
        'Duración de la Partida',
        '-TIEMPO-',
        ['1 minuto', '1:30 minutos', '2 minutos', '3 minutos', '5 minutos'],
        '2 minutos'
    )

    pistas = sg.Checkbox(
        text='Pistas',
        background_color=colors.PRIMARY_LIGHT,
        font=('courier', 20),
        text_color=colors.BLACK
    )

    guardar = sg.Button(
        button_text='Guardar',
        key='-GUARDAR-',
        font=('courier', 13),
        size=(25, 3)
    )

    mid_sep = sg.Text(background_color=colors.PRIMARY_LIGHT, size=(1, None))

    cancelar = sg.Button(
        button_text='Cancelar',
        key='-CANCELAR-',
        font=('courier', 13),
        size=(25, 3)
    )

    return sg.Window(
        title='',
        layout=[
            [exitbar_widget.build(colors.PRIMARY_LIGHT)],
            [title],
            [separator_widget.separator2(colors.PRIMARY_LIGHT, colors.BLACK)],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
            [casillas],
            [coincidencias],
            [tipo_elementos],
            [tiempo],
            [pistas],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
            [guardar, mid_sep, cancelar],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
        ],
        no_titlebar=True,
        keep_on_top=True,
        grab_anywhere=True,
        background_color=colors.PRIMARY_LIGHT,
        element_justification='c',
        finalize=True
    )
"""Ventana que permite elegir y visualizar los distintos criterios."""
import PySimpleGUI as sg
from src.windows import colors
from src.windows.widgets import option_widget


sg.theme('reddit')

def build():
    titulo = sg.Text(
        text='Combine para visualizar los resultados',
        font=('times', 25),
        text_color=colors.BLACK,
        background_color=colors.BACKGROUND,
    )

    explicacion = sg.Text(
        text='Tenga en cuenta que la selección en algunos días\ny en diferentes horas puede repetirse',
        justification='c',
        font=('times', 15),
        text_color=colors.BLACK,
        background_color=colors.BACKGROUND,
    )
    
    selec_dia_semana = option_widget.build(
        'Dia de la Semana',
        '-DIA-',
        ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
        'Lunes'
    )

    selec_horario = option_widget.build(
        'Rango Horario', 
        '-RANGO-',
        ['Madrugada (0, 6)', 'Mañana (6, 12)', 'Tarde (12, 18)', 'Noche (18, 24)'],
        'Madrugada (0, 6)'
    )

    realizar = sg.Button(
        'Obtener Selección',
        size=(30, 2),
        button_color=(colors.WHITE, colors.PRIMARY_LIGHT),
        mouseover_colors=(colors.PRIMARY_LIGHT, colors.WHITE),
        key='-REALIZAR-'
    )

    return sg.Window(
        title='Criterios de seleccion',
        layout=[
            [titulo],
            [explicacion],
            [selec_dia_semana],
            [selec_horario],
            [realizar]
        ],
        element_justification='c',
        finalize=True,
        background_color=colors.BACKGROUND
    )
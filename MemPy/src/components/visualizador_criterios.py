import PySimpleGUI as sg

from src.windows import visualizador_criterios
from src.handlers import visualizador_criterios_handlers


def start():
    window = visualizador_criterios.build()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        visualizador_criterios_handlers.mostrar_resultados(values['-DIA-'], values['-RANGO-'])

    window.close()
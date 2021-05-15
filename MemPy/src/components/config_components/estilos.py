from src.windows.config_windows import estilos
from src.components import config_json


def start(nivel):
    window = estilos.build()

    while True:
        event, values = window.read()

        if event in ('-SALIR-', '-CANCELAR-'):
            break
        if event == '-GUARDAR-':
            tema=values['-TEMA-']
            config_json.set_config_config(nivel,tema)
            break

    window.close()
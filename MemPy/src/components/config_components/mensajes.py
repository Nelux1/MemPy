from src.windows.config_windows import mensajes
from src.components import config_json

def start(nivel):
    window = mensajes.build()

    while True:
        event, values = window.read()

        if event in ('-SALIR-', '-CANCELAR-'):
            break
        if event == '-GUARDAR-':

            ganador= values['-WIN_MESSAGE-']
            perdedor=values['-LOSS_MESSAGE-']
            tiempo= values['-TIMELEFT_MESSAGE-']
            config_json.set_config_mensajes(nivel,ganador,perdedor,tiempo)
            break          


    window.close()
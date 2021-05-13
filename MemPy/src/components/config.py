"""Loop de la ventana de configuraciones."""
from src.windows import config

from src.components import config_mensajes, config_partida


def start():
    window = config.build()

    while True:
        event, values = window.read()

        if event == '-SALIR-':
            break

        window.hide()
        if event == '-MENSAJES-':
            config_mensajes.start()
        elif event == '-PARTIDA-':
            config_partida.start()
        # else:
        #     config_personalizacion.start()
        window.un_hide()


    window.close()
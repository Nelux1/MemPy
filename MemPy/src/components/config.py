"""Loop de la ventana de configuraciones.

    Interactua con las ventanas/loops en components/config_components.
"""
from src.windows import configuraciones

from src.components.config_components import mensajes, partida, estilos


def start():
    window = configuraciones.build()

    while True:
        event, values = window.read()

        if event in ('-SALIR-', '-BACK-'):
            break

        window.hide()

        if event == '-MENSAJES-':
            mensajes.start()
        elif event == '-PARTIDA-':
            partida.start()
        else:
            estilos.start()

        window.un_hide()


    window.close()









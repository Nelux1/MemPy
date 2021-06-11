"""Loop de la ventana de configuraciones.

    Interactua con las ventanas/loops en components/config_components.
"""
from src.windows import configuraciones
from src.models.user_repository import UserRepository
from src.components.config_components import mensajes, partida, estilos

def start():
    window = configuraciones.build()

    while True:
        event, values = window.read()

        if event in ('-SALIR-', '-BACK-'):
         break

        window.hide()

        nivel = values['-NIVEL-'] - 1
        if event == '-MENSAJES-':
            mensajes.start(nivel)
        elif event == '-PARTIDA-':
            partida.start(nivel)
        else:
            estilos.start(nivel)

        # serializa las configuraciones hechas
        UserRepository.serializar_actual()

        window.un_hide()
    window.close()









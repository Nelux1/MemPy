import PySimpleGUI as sg

from src.windows import login
from src.components import registro, inicio
from src.models.user_repository import UserRepository


def start():
    window = login.build()

    while True:
        event, values = window.read()

        if event == '-SALIR-':
            break

        username = values['-USERNAME-']

        # inválido = input vacío.
        if not username:
            print('Usuario inválido')
        else:
            # si no existe, lo registra
            if not UserRepository().existe_usuario(username):
                # si se registró bien, puede abrir la ventana inicio
                if registro.start(username):
                    break
            # si existía, puede abrir la ventana inicio
            else:
                break

    window.close()

    # sólo se abre la ventana inicio si el evento no fue de salir
    if event != '-SALIR-':    
        inicio.start()
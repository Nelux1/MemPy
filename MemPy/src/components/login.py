from src.models.user import User
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

        # si se ingresó un nombre de usuario
        if username:
            usuario = UserRepository.obtener_usuario(username)

            window.hide()

            # si el usuario no está registrado
            if not usuario:
                usuario = registro.start(username)
            
            # si el usuario existía o se registró correctamente
            if usuario:
                UserRepository.current_user = usuario
                break

            window.un_hide()
        

    window.close()

    # si se logeo un usuario
    if event != '-SALIR-':
        inicio.start()
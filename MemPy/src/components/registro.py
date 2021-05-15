from src.windows import registro

from src.models.user import User
from src.models.user_repository import UserRepository
from src.handlers import validation_handlers as validation


def start(username):
    window, usuario = loop(username)
    window.close()
    return usuario


def loop(username):
    window = registro.build()
    usuario = None

    while True:
        event, values = window.read()

        if event in ('-SALIR-', '-BACK-'):
            break

        edad = values['-EDAD-']
        genero = values['-GENERO-']

        if validation.are_valid_credentials(edad, genero):
            UserRepository.agregar_usuario((usuario := User(username, genero, edad)))
            break
        
    return (window, usuario)
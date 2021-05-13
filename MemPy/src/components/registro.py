from src.windows import registro

from src.models.user import User
from src.models.user_repository import UserRepository


def start(username):
    window = registro.build()

    while True:
        event, values = window.read()

        if event in ('-SALIR-', '-BACK-'):
            break

        if event == '-REGISTRARSE-':
            edad = values['-EDAD-']
            genero = values['-GENERO-']

            # pequeña validación de los datos ingresados
            if not edad.isdigit() or not genero:
                print('Datos inválidos')
            else:
                UserRepository().agregar_usuario(User(username, genero, edad))
                break
        
    window.close()

    if event not in ('-SALIR-', '-BACK-'):
        return True
    return False
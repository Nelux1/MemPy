from src.windows import registro

from src.models.user import User
from src.models.user_repository import UserRepository


def start (username):
    window = registro.build()
    event,values= window.read(close = True)
    if event == '-REGISTRARSE-':
        usu_gen=values['-GENERO-']
        usu_edad=values['-EDAD-']
        repositorio = UserRepository()
        user = User(username,usu_gen,usu_edad)
        repositorio.agregar_usuario(user)
        return True
    return False

from src.models import user_repository
from src.models.user_repository import UserRepository
from src import windows
from src.windows import registro
from src.models.user_repository import UserRepository
from src.models.user import User

window = registro.build()

def start (username):
    while True:
        event,values= window.read()
        if event == '-SALIR-':
            break
        usu_gen=values['-GENERO-']
        usu_edad=values['-EDAD-']
        repositorio = UserRepository()
        user = User(username,usu_gen,usu_edad)
        repositorio.agregar_usuario(user)

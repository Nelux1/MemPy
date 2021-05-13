from src.windows import login
import PySimpleGUI as sg
from src.models.user_repository import UserRepository
from src.components import registro, inicio



def start():
    window= login.build()
    while True:
        event,values= window.read()
        if event == '-SALIR-':
            break
        usu=values['-USERNAME-']  
        repository= UserRepository()
        objusuario=repository.existe_usuario(usu)
        if objusuario is False:
            reg_exito = registro.start(usu)
        if objusuario or reg_exito:
            break  
    window.close()
    inicio.start()  
from src.models.user import User
from src.windows import inicio
from src.components import config, puntajes, estadisticas,jugar
from src.models.user_repository import UserRepository

def start():
    window = inicio.build()
    
    while True:
        event, values = window.read()
        
        if event == '-SALIR-':
            break
        
        window.hide()

        if event == '-CONFIG-':
            config.start()
        elif event == '-ESTADISTICAS-':
            estadisticas.start()
        elif event == '-PUNTAJES-':
            puntajes.start(UserRepository.current_user.username ,
                           UserRepository.current_user.puntaje)
        elif event == '-JUGAR-':
            jugar.start(UserRepository.current_user.username , 
                        UserRepository.current_user.config ,
                        UserRepository.current_user.age , 
                        UserRepository.current_user.gender ,
                        UserRepository.current_user.puntaje )

        window.un_hide()

    window.close()
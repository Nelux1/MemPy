from src.models.user_repository import UserRepository


def set_config_mensajes(nivel, mensaje_gana, mensaje_pierde, mensaje_tiempo):
    UserRepository.current_user.config[nivel]['-WIN_MESSAGE-'] = mensaje_gana
    UserRepository.current_user.config[nivel]['-LOSS_MESSAGE-'] = mensaje_pierde
    UserRepository.current_user.config[nivel]['-TIMELEFT_MESSAGE-'] = mensaje_tiempo


def set_config_partida(nivel, casillas, coincidencias, elementos, tiempo, pistas):
    UserRepository.current_user.config[nivel]['-CASILLAS-'] = casillas
    UserRepository.current_user.config[nivel]['-COINCIDENCIAS-'] = coincidencias
    UserRepository.current_user.config[nivel]['-ELEMENTOS-'] = elementos
    UserRepository.current_user.config[nivel]['-TIEMPO_MIN-'] = tiempo
    UserRepository.current_user.config[nivel]['-PISTAS-'] = pistas


def set_config_estilo(nivel, tema):
    UserRepository.current_user.config[nivel]['-TEMA-'] = tema

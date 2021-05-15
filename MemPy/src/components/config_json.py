import json
import os

datos = os.path.join(os.getcwd(), 'users.json')


def set_config_mensajes(nivel, mensaje_gana, mensaje_pierde, mensaje_tiempo):
    archivo = open(datos)
    data = json.load(archivo)
    archivo.close()
    archivo = open(datos, 'w', encoding='UTF-8')
    data[0]['config'][nivel]['-WIN_MESSAGE-'] = mensaje_gana
    data[0]['config'][nivel]['-LOSS_MESSAGE-'] = mensaje_pierde
    data[0]['config'][nivel]['-TIMELEFT_MESSAGE-'] = mensaje_tiempo
    json.dump(data, archivo)
    archivo.close()


def set_config_partida(nivel, casillas, coincidencias, elementos, tiempo, pistas):
    archivo = open(datos)
    data = json.load(archivo)
    archivo.close()
    archivo = open(datos, 'w', encoding='UTF-8')
    data[0]['config'][nivel]['-CASILLAS-'] = casillas
    data[0]['config'][nivel]['-COINCIDENCIAS-'] = coincidencias
    data[0]['config'][nivel]['-ELEMENTOS-'] = elementos
    data[0]['config'][nivel]['-TIEMPO_MIN-'] = tiempo
    data[0]['config'][nivel]['-PISTAS-'] = pistas
    json.dump(data, archivo)
    archivo.close()


def set_config_config(nivel, tema):
    archivo = open(datos)
    data = json.load(archivo)
    archivo.close()
    archivo = open(datos, 'w', encoding='UTF-8')
    data[0]['config'][nivel]['-TEMA-'] = tema
    json.dump(data, archivo)
    archivo.close()

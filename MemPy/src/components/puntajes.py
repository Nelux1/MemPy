from PySimpleGUI.PySimpleGUI import Window
from src.windows import puntajes


def start(username,puntaje):
    window = puntajes.build(username,puntaje)

    while True:
        event, values = window.read()

        if event == '-SALIR-' or Window.close:
            break

    window.close()
from tkinter import colorchooser
import PySimpleGUI as sg
from src.windows import colors
from src.windows import jugar


def start():
    window = jugar.build()

    while True:
        event, values = window.read()
        
        if event == '-SALIR-':
            break
        elif event == ("-imagen-"):
            pass
                        


    window.close()
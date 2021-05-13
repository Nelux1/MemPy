from tkinter import Event
from src import windows
from src.windows import inicio

def start():
    window = inicio.build()
    while True:
        event, values = window.read()
        if event == '-SALIR-':
            break
    window.close()
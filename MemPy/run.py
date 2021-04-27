"""Punto de inicio la aplicación."""
# from src import mempy

# if __name__ == '__main__':
#     mempy.run()
    


# TESTEO DE LAS VENTANAS

from src.servicio_login.views import login

if __name__ == '__main__':
    event, values = login.build().read(close=True)

from src.servicio_login.views import register

if __name__ == '__main__':
    event, values = register.build().read(close=True)
    
from src.servicio_inicio.views import inicio

if __name__ == '__main__':
    window1 = inicio.build()
    event, values = window1.read(close=True)
        
# import PySimpleGUI as sg
# from src.globals.elements import custom_input, custom_button

# if __name__ == '__main__':
#     event, values = sg.Window('', layout=[[custom_input('mi input', 'in', '#000', '#FFF', '#FFF')], [custom_button('enviar', 'send')]], resizable=True).read(close=True)
        
import os

import PySimpleGUI as sg


def build(color):
    """Retorna una barra con una X de salida a la derecha. 

        Parámetros
        ----------
            color : str
                valor hexa para el color de fondo de la barra
    
        Return
        ------
            bar : sg.Column
    """
    exit_bttn = sg.Button(
                            key='-SALIR-',
                            tooltip='Salir',
                            pad=((0, 10), (10, 0)),
                            border_width=0,
                            button_color=(color, color),
                            image_filename=os.path.join('resources', 'icons', 'outline_close_black_48dp.png'),
                            image_size=(20, 20),
                            image_subsample=4
                        )
    
    return sg.Column(
        layout=[[exit_bttn]], 
        background_color=color, 
        expand_x=True, 
        element_justification='r'
    )
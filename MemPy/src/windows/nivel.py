import PySimpleGUI as sg
from src.windows import colors
from src.windows.widgets import separator_widget


def popup_nivel():
    """se selecciona el nivel para jugar"""
    title = sg.Text(
        text='SELECCIONE\n EL NIVEL',
        font=('times', 20, 'bold'),
        background_color=colors.BACKGROUND,
        text_color=colors.BLACK,
        size=(30, 3),
        justification='c'
    )

    
    return sg.Window(
        title='',
     layout=[
            [title], 
            [sg.Button('Nivel 1',font=('times'), button_color=(colors.BLACK))],
            [sg.Button('Nivel 2',font=('times'), button_color=(colors.BLACK))],
            [sg.Button('Nivel 3',font=('times'), button_color=(colors.BLACK))],
            [separator_widget.estilo2(colors.BACKGROUND, colors.BLACK)],
            [sg.Text('En la seccion configuraciones puedes configurar cada nivel',
            font=('times',15),text_color=colors.BLACK,background_color=colors.BACKGROUND)],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 2)],              
        ],    


        element_justification='c',
        background_color=colors.BACKGROUND,
    )

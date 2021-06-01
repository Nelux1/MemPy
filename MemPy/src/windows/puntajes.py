import PySimpleGUI as sg
from src.windows import colors
from src.windows.widgets import exitbar_widget, separator_widget
from src.components.posiciones import positions

def build(username,puntaje):
    title = sg.Text(
        text='', 
        font=('times', 30, 'bold'),
        background_color=colors.PRIMARY_LIGHT,
        text_color=colors.WHITE,
        size=(45, 8),
        justification='c'
    )
    
    return sg.Window(
        title='Puntajes',
        layout=[
            [exitbar_widget.build(colors.PRIMARY_LIGHT)],   
            [sg.Text(text= 'POSICIONES',background_color=colors.PRIMARY_LIGHT,text_color=colors.WHITE,font=('times', 30, 'bold'))],         
            [sg.Text(text= '*' * 80, background_color=colors.PRIMARY_LIGHT, text_color=colors.BLACK, font=('times', 10, 'bold'))],
            [sg.Text(text= '  JUGADOR                 PUNTAJE              PUESTO', background_color=colors.PRIMARY_LIGHT, text_color=colors.WHITE, font=('times', 15, 'bold'))],   
            [sg.Text(text= positions(),background_color=colors.PRIMARY_LIGHT, text_color=colors.BLACK, font=('times', 20, 'bold'))],
            [title]
        ],
        background_color=colors.PRIMARY_LIGHT,
        no_titlebar=True,
        element_justification='c',
        keep_on_top=True,
        finalize=True    
    )

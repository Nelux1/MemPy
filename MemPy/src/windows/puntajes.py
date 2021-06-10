import PySimpleGUI as sg
from src.windows import colors
from src.windows.widgets import exitbar_widget
from src.components.posiciones import posiciones

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
            [sg.Table(values=[posiciones(username,puntaje)][:],max_col_width=1, 
            auto_size_columns=True,num_rows=5,row_height=5,background_color=colors.PRIMARY_LIGHT,
             text_color=colors.WHITE, font=('times',10,'bold'))
            ],
            [title]
        ],
        background_color=colors.PRIMARY_LIGHT,
        no_titlebar=True,
        element_justification='c',
        keep_on_top=True,
        finalize=True    
    )

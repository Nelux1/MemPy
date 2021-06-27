import os
import PySimpleGUI as sg
from src.windows import colors
from src.windows.widgets import exitbar_widget, separator_widget ,abandonar_widget
from src.handlers.jugar_config import cuadros, pistas, mensajes



cart= os.path.join(
    'resources', 
    'icons', 
    'inte.png'
)

TABLERO_ICON= os.path.join(
    'resources', 
    'icons', 
    'copa.png'
)

def build(username,configu,n,board_data):
    
    title= sg.Text(
    text='MEMPY',
    font=('courier',30),
    background_color=colors.BACKGROUND,
    text_color=colors.BLACK,
    size=(30,2),
    justification='c'
    )
    copa = sg.Image(
        filename=TABLERO_ICON, 
        background_color=colors.BACKGROUND
    )

    column_info = sg.Column(
        layout=[
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 5)],
            [copa],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 2)],
            [sg.Text(f'{mensajes(configu,n)}',key='-POCO-TIEMPO-', background_color=colors.BACKGROUND, text_color=colors.RED, font=('times',15, 'bold'),visible=False)],
            [sg.Text(text=f'Jugador: {username}', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))],
            [sg.Text(text=f'Tiempo x ficha:', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))]+
            [sg.Text(text_color=colors.BLACK,size= (6,1), background_color=colors.BACKGROUND, key='-TIEMPO-PASO-',font=('times',15),justification='center')],
            [sg.Text(text=f'Nivel:', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))]+
            [sg.Text(text_color=colors.BLACK,size= (6,1), background_color=colors.BACKGROUND, key='-NIV-',font=('times',15),justification='center')],
            [sg.Text(text='Tiempo:', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))] +
            [sg.Text(text_color=colors.BLACK,size= (6,1), background_color=colors.BACKGROUND, key='-TIMER-',font=('times',15),justification='center')],
            [sg.Text(text='Tiempo total:', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))] +
            [sg.Text(text_color=colors.BLACK,size= (6,1), background_color=colors.BACKGROUND, key='-REAL_TIME-',font=('times',15),justification='center')],
            [sg.Text(text='Palabras:',text_color=colors.BLACK,size= (8,1), background_color=colors.BACKGROUND,font=('times',15,'bold'))],
            [sg.Text(text='',text_color=colors.BLACK,size= (6,1), background_color=colors.BACKGROUND, key='-ENCONTRADOS-',font=('times',15,'bold'))],
            [sg.Button('PISTA',font=('times'), button_color=colors.BLACK, visible= pistas(configu,n),size= (3,1))],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 4)]
        ],


        
        background_color=colors.BACKGROUND,
        element_justification='c',
    ) 
    game_column = sg.Column(
                    layout=[    
                    [sg.Button(board_data[x][y], key=f'pieza-{x}-{y}',image_filename=cart,image_size=(70,70),pad= (3,3),button_color=
                    (colors.BACKGROUND,colors.WHITE))
                    for x in range (cuadros(configu,n))] for y in range(4)],
                    background_color=colors.BACKGROUND,
                    element_justification='c',
                    pad=(20, 10)
                )

    layout=[
        [exitbar_widget.build(colors.PRIMARY_DARK)],
        [title]+[abandonar_widget.build(colors.BACKGROUND)],
        [sg.Text(background_color=colors.BACKGROUND, size=(3, None)), column_info, game_column, sg.Text(background_color=colors.BACKGROUND, size=(2, None))],
        [separator_widget.invisible_horizontal(colors.BACKGROUND, 5)]   
    ]
    
    
    return sg.Window(
        title='MemPy',
        layout=layout,
        background_color=colors.BACKGROUND,
        element_justification='c',
        finalize=True,
        keep_on_top=True,
        no_titlebar=True
        
    ) 
    
    

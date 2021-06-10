import os
import PySimpleGUI as sg
from src.windows import colors
from src.windows.widgets import exitbar_widget, separator_widget



cart= os.path.join(
    'resources', 
    'icons', 
    'inte.png'
)

def build(username,configu):
    
    title= sg.Text(
    text='MEMPY',
    font=('courier',25),
    background_color=colors.BACKGROUND,
    text_color=colors.BLACK,
    size=(30,2),
    justification='c'
    )
    
    column_info = sg.Column(
        layout=[
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 10)],
            [sg.Text(text=f'Jugador: {username}', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))],
            [sg.Text(text='Tiempo:', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))] +
            [sg.Text(text_color=colors.BLACK,size= (6,1), background_color=colors.BACKGROUND, key='-TIMER-',font=('times',15),justification='center')],
            [sg.Text(text='Tiempo total:', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))] +
            [sg.Text(text_color=colors.BLACK,size= (6,1), background_color=colors.BACKGROUND, key='-REAL_TIME-',font=('times',15),justification='center')],
            [sg.Text('Elementos encontrados {} de {}', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 10)],
            [sg.Button('PISTA',font=('times'), button_color=colors.BLACK)],
        ],


        
        background_color=colors.BACKGROUND,
        element_justification='c',
        expand_y=True,
    ) 
    game_column = sg.Column(
                    layout=[    
                    [sg.Button(image_filename=cart,image_size=(50,50), key=f'pieza-{x},{y}',pad= (3,3),button_color=
                    (colors.BACKGROUND,colors.WHITE),mouseover_colors=(colors.BLACK, colors.BLACK)) 
                    for x in range (8)] for y in range(8)],
                    background_color=colors.BACKGROUND,
                    element_justification='c',
                    expand_y=True,
                    pad=(20, 10)
                )
    layout=[
        [exitbar_widget.build(colors.PRIMARY_DARK)],
        [title],
        [separator_widget.invisible_horizontal(colors.BACKGROUND, 3)],
        [sg.Text(background_color=colors.BACKGROUND, size=(3, None)), column_info, game_column, sg.Text(background_color=colors.BACKGROUND, size=(2, None))],
        [separator_widget.invisible_horizontal(colors.BACKGROUND, 3)]
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
    
    

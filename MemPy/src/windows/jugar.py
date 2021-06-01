import os
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ConvertArgsToSingleString, button_color_to_tuple
from src.windows import colors
from src.windows.widgets import exitbar_widget, separator_widget


cart= os.path.join(
    'resources', 
    'icons', 
    'inte.png'
)

def build(username):
    column_info = sg.Column(
        layout=[
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 10)],
            [sg.Text(text=f'Jugador: {username}', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))],
            [sg.Text('Tiempo del paso actual {}', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))],
            [sg.Text('Tiempo total {}', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))],
            [sg.Text('Elementos encontrados {} de {}', background_color=colors.BACKGROUND, text_color=colors.BLACK, font=('times', 15, 'bold'))],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 10)],
            [sg.Button('PISTA',font=('times'), button_color=colors.BLACK)]
        ],
        background_color=colors.BACKGROUND,
        element_justification='c',
        expand_y=True,
    ) 
    game_column = sg.Column(
                    layout=[[sg.Button(image_filename=cart,image_size=(50,50),pad= (5,5),button_color=
                    (colors.WHITE,colors.WHITE),mouseover_colors=(colors.PRIMARY_LIGHT, colors.PRIMARY_LIGHT)) 
                    for x in range (8)] for y in range(8)],
                    background_color=colors.WHITE,
                    element_justification='c',
                    expand_y=True,
                    pad=(20, 10)
                )
    layout=[
        [exitbar_widget.build(colors.PRIMARY_DARK)],
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
    
    

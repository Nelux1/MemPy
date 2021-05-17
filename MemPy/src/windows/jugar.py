import PySimpleGUI as sg
from src.windows import colors
from src.windows.widgets import exitbar_widget


def build():
    title=sg.Text(
        text='MemPy',
        font=('Courier',35, ''),
        background_color=colors.PRIMARY_LIGHT,
        text_color=colors.BLACK,
        size=(30,2),
        justification='c')
       
    layout=[
            [exitbar_widget.build(colors.PRIMARY_DARK)],
            [title]
        ]
    
    
    for y in range (8):
        layout+=[
        [[sg.Button(" ",size= (5,3), key="-imagen-")for x in range (8)]]
    ]   
    
    return sg.Window(title='MemPy',
            
        background_color=colors.PRIMARY_LIGHT,
        element_justification='c'
    ).layout(layout)   
    
    

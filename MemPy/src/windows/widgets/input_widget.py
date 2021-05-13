import PySimpleGUI as sg

from src.windows import colors


LABEL_FONT = ('Courier', 13)
INPUT_FONT = ('Courier', 20)
INPUT_UNDERLINE = ('Courier', 1, 'underline')


def build(text, key, background_color, text_color, focus=False):
    """Retorna una barra de input con estilo pseudo moderno.
    
    
        Parametros
        ----------
            text : str
                texto indicador arriba del input
            key : str
                clave que va a tener el objeto input
            focus : boolean
                si el input va a tener focus o no

            el resto son parámetros de personalización.
    """

    # texto indicador arriba del campo de input
    label = sg.Text(
        text=text, 
        background_color=background_color, 
        text_color=text_color, 
        font=LABEL_FONT
    )

    # espacio entre label y el campo de input
    space = sg.Text('', size=(0, 1), background_color=background_color)

    # el objeto input
    input_elem = sg.Input(
        key=key, 
        size=(15, None), 
        border_width=0, 
        background_color=background_color,
        text_color=text_color, 
        font=INPUT_FONT, 
        justification='c', 
        focus=focus
    )

    # imaginar que es parte del obj input también
    input_underline = sg.Text(
        '_'*248,
        text_color=colors.BLACK,
        background_color=background_color, 
        font=INPUT_UNDERLINE
    )
        
    return sg.Column(
        layout=[
            [label], 
            [space], 
            [input_elem], 
            [input_underline]
        ], 
        background_color=background_color,
        element_justification='c'
    )
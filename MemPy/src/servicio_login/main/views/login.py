import PySimpleGUI as sg


# global settings
sg.set_options(
    font='Fixedsys',
    button_color=('#FFF', '#238FFB'),
    auto_size_buttons=False,
    button_element_size=(15, 3),
    margins=(0, 0),
    element_padding=(0, 0)
)


def build_header():
    """Retorna una columna que contiene el header."""
    top_filler = sg.Text('',                  size=(0, 4), background_color='#238FFB')
    title = sg.Text('MemPy',                              background_color='#238FFB', font=('Fixedsys', 50))
    subtitle = sg.Text('El Clásico Juego de la Memoria', background_color='#238FFB', font=('Fixedsys', 20))
    bottom_filler = sg.Text('',               size=(0, 4), background_color='#238FFB')
    
    header_elements = [
        [top_filler],
        [title],
        [subtitle],
        [bottom_filler]
    ]
    
    header_container = sg.Column(layout=header_elements, background_color='#238FFB', expand_x=True, element_justification='c')
    
    return header_container


def build_body():
    """Retorna una columna que contiene el body."""
    top_filler = sg.Text('', size=(0, 4), background_color='#FFF')
    
    username_text =  sg.Text('Nombre de Usuario', background_color='#FFF',                text_color='#238FFB', font=('Fixedsys', 17))
    input_username = sg.Input(key='-USERNAME-', size=(20, None), pad=(0, 15),             text_color='#1F1F1F', font=('Fixedsys', 17), justification='c')
    
    login_bttn = sg.Button('Entrar')
    exit_bttn =  sg.Button('Salir', pad=(12, 0))
    middle_filler = sg.Text('', size=(5, 5), background_color='#FFF')
    
    body_elements = [
        [top_filler],
        [username_text],
        [input_username],
        [login_bttn, middle_filler, exit_bttn]
    ]
    
    body_container = sg.Column(layout=body_elements, background_color='#FFFFFF', expand_x=True, expand_y=True, element_justification='c')

    return body_container

def build():
    layout = [
        [build_header()],
        [build_body()]
    ]
    
    window = sg.Window('', layout=layout, alpha_channel = 0.97, no_titlebar=True, grab_anywhere=True, size=(600, 600))
    
    return window


if __name__ == '__main__':
    event, values = build().read(close=True)
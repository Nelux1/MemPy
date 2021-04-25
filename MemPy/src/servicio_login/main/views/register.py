# TODO crear ventana que pregunte si se quiere registrar!
import PySimpleGUI as sg


# global settings
sg.set_options(
    font='Fixedsys',
    button_color=('#FFF', '#238FFB'),
    auto_size_buttons=False,
    button_element_size=(16, 3),
    margins=(0, 0),
    element_padding=(0, 0)
)


def build_header():
    """Retorna una columna que contiene el header."""
    top_filler = sg.Text('',                  size=(0, 4), background_color='#238FFB')
    title = sg.Text('Registro', background_color='#238FFB', justification='center', font=('Fixedsys', 50))
    subtitle = sg.Text('Por favor, complete los campos', background_color='#238FFB', justification='center', font=('Fixedsys', 20))
    bottom_filler = sg.Text('',               size=(0, 4), background_color='#238FFB')

    header_elements = [
        [top_filler],
        [title],
        [subtitle],
        [bottom_filler]
    ]

    header_container = sg.Column(layout=header_elements, background_color='#238FFB', expand_x=True, element_justification='center')

    return header_container


def build_body():
    """Retorna una columna que contiene el body."""
    top_filler = sg.Text('',                  size=(0, 2), background_color='#FFF')
    
    gender_text = sg.Text('Género', background_color='#FFF', text_color='#238FFB', font=('Fixedsys', 17))
    gender_input = sg.Input(key='-GENDER-', text_color='#1F1F1F', size=(20, None), font=('Fixedsys', 17), justification='center')
    
    inputs_middle_filler = bttns_middle_filler = sg.Text('', size=(0, 1), background_color='#FFF')
    
    age_text = sg.Text('Edad', background_color='#FFF', text_color='#238FFB', font=('Fixedsys', 17))
    age_input = sg.Input(key='-AGE-', text_color='#1F1F1F', size=(20, None), font=('Fixedsys', 17), justification='center')
    
    register_bttn = sg.Button('Registrarse')
    bttns_middle_filler = sg.Text('', size=(5, 8), background_color='#FFF')
    back_bttn = sg.Button('Volver Atrás')
    
    body_elements = [
        [top_filler],
        [gender_text],
        [gender_input],
        [inputs_middle_filler],
        [age_text],
        [age_input],
        [register_bttn, bttns_middle_filler, back_bttn]
    ]

    body_container = sg.Column(layout=body_elements, background_color='#FFF', expand_x=True, expand_y=True, element_justification='center')

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
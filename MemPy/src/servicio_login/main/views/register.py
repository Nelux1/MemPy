import PySimpleGUI as sg


def build_header():
    """Retorna un elemento header(Column), para agregar a un layout."""

    # Layout for the elements.
    layout = [
        [sg.Text('Registro', background_color='#238FFB', justification='center', font=('Fixedsys', 40))],
        [sg.Text('Por favor, ingrese los datos', background_color='#238FFB', justification='center', font=('Fixedsys', 10))]
    ]

    # Container for the elements.
    elements_container = sg.Column(layout, pad=(102, 50), background_color='#238FFB', element_justification='center')

    # Container of the header (used for centering & coloring the background).
    header = sg.Column([[elements_container]], pad=(0, 0), size=(475, 200), background_color='#238FFB', element_justification='center')

    return header


def build_body():
    """Retorna un elemento body(Column), para agregar a un layout."""
    
    # Layout for the elements.
    layout = [
        [sg.Text('Género', background_color='#FFF', text_color='#238FFB')],
        [sg.Input(key='-GENDER-', pad=((0, 0), (3, 10)), text_color='#1F1F1F', size=(15, 2), font=('Fixedsys', 17), justification='center')],
        [sg.Text('Edad', background_color='#FFF', text_color='#238FFB')],
        [sg.Input(key='-AGE-', pad=((0, 0), (3, 10)), text_color='#1F1F1F', size=(15, 2), font=('Fixedsys', 17), justification='center')],
        [sg.Button('Registrarse', pad=(0, 10), button_color='#238FFB', size=(15, 2)), sg.T('', background_color='#FFF', size=(1, 0)), sg.Button('Volver Atrás', size=(15, 2), button_color='#238FFB')]
    ]

    # Container for the elements
    elements_container = sg.Column(layout, pad=(90, 35), background_color='#FFF', element_justification='center')

    # Container of the header (used for centering & coloring the background).
    body = sg.Column([[elements_container]], pad=(0, 0), size=(475, 400), background_color='#FFF', element_justification='center') 

    return body


def build():
    layout = [[build_header()], [build_body()]]
    
    window = sg.Window('', layout=layout, alpha_channel = 0.97, no_titlebar=True, grab_anywhere=True, size=(475, 475), margins=(0, 0), element_justification='center', font=('Fixedsys', 15))
    
    return window


if __name__ == '__main__':
    event, values = build().read(close=True)
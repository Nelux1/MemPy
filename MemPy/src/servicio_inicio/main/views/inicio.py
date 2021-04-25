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


def build_exit_bar():
    """Retorna una columna que contiene un barra con botón de salida."""
    exit_bttn = sg.Button('', pad=(8, 8), border_width=0, button_color=('#238FFB', '#238FFB'), image_filename='resources\icons\outline_close_black_24dp.png', image_size=(17, 17), image_subsample=2)
    return sg.Column([[exit_bttn]], background_color='#238FFB', expand_x=True, element_justification='r')


def build_header():
    """Retorna una columna que contiene el header."""
    top_filler = sg.Text('',                  size=(0, 4), background_color='#238FFB')
    title = sg.Text('Mempy', background_color='#238FFB', justification='center', font=('Fixedsys', 50))
    subtitle = sg.Text('', background_color='#238FFB', justification='center', font=('Fixedsys', 20))
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
    top_filler = sg.Text('',                  size=(0, 5), background_color='#FFF')

    play_bttn = sg.Button('Jugar')
    between_filler1 = sg.Text('', size=(4, 0), background_color='#FFF')
    statistics_bbtn = sg.Button('Estadísticas')
    
    middle_filler = sg.Text('', size=(0, 2),  background_color='#FFF')
    
    scores_bttn = sg.Button('Puntajes')
    between_filler2 = sg.Text('', size=(4, 0), background_color='#FFF')
    config_bttn = sg.Button('Configuración')
    
    body_elements = [
        [top_filler],
        [play_bttn, between_filler1, statistics_bbtn],
        [middle_filler],
        [scores_bttn, between_filler2, config_bttn]
    ]

    body_container = sg.Column(layout=body_elements, background_color='#FFF', expand_x=True, expand_y=True, element_justification='center')

    return body_container


def build():
    layout = [
        [build_exit_bar()],
        [build_header()],
        [build_body()]
    ]
    
    window = sg.Window('', layout=layout, alpha_channel = 0.97, no_titlebar=True, grab_anywhere=True, size=(600, 600))
    
    return window


if __name__ == '__main__':
    event, values = build().read(close=True)
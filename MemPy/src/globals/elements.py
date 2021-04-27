"""Este módulo contiene métodos para crear widgets compuestos.

    También están acá porque hay varios estilos que se repiten siempre.
"""

import PySimpleGUI as sg

import src.globals.colors as colors
import src.globals.fonts as fonts
import src.globals.texts as texts
import src.globals.sizes as sizes

import src.globals.paths as paths


def separator1(background_color, text_color):
    """Crea un separador con signos de igual."""
    return sg.Text('═'*66, text_color=text_color, background_color=background_color)


def separator2(background_color, text_color):
    """Crea un separador del estilo ubicado en texts.py"""
    return sg.Text(texts.SEPARATOR, background_color=background_color, text_color=text_color)


def exit_bttn_bar(color):
    """Retorna una barra con una X de salida a la derecha. 
    
        Return
        ------
            bar : sg.Column
    """
    exit_bttn = sg.Button(
                            key='-SALIR-',
                            tooltip='Salir',
                            pad=((0, 10), (10, 0)),
                            border_width=0,
                            button_color=(color, color),
                            image_filename=paths.EXIT_ICON,
                            image_size=(20, 20),
                            image_subsample=4
                        )
    
    bar = sg.Column([[exit_bttn]], background_color=color, expand_x=True, element_justification='r')
    
    return bar


def custom_input(text, key, background_color, text_color, input_line_color, focus=False):
    """Retorna una barra de input personalizada
    
        Return
        ------
            custom_input : sg.Column
    """
    label =  sg.Text(text=text, background_color=background_color, text_color=text_color, font=fonts.LABEL_FONT)
    space = sg.Text('', size=(0, 1), background_color=background_color)
    input_elem = sg.Input(key=key, size=(15, None), border_width=0, background_color=background_color, text_color=text_color, font=fonts.INPUT_FONT, justification='c', focus=focus)
    input_underline = sg.Text('_'*248, text_color=input_line_color, background_color=background_color, font=fonts.INPUT_UNDERLINE)
    
    custom_input = sg.Column([[label], [space], [input_elem], [input_underline]], background_color=background_color, element_justification='c')
    
    return custom_input


def custom_button(text, key=None, size=(30, 2), button_color=('#FFF', colors.SECONDARY), bind_return_key=False, pad=(None, None)):
    """Retorna un botón personalizado.
    
        Return
        ------
            button : sg.Button
    """
    return sg.Button(button_text=text, border_width=0, key=key, font=fonts.BTTN_FONT, size=size, button_color=button_color, bind_return_key=bind_return_key, pad=pad)


def header(icon_filepath, background_color, title, separator, subtitle=''):
    """Retorna un header con logo, titulo y subtitulo.
    
        Return
        ------
            header : sg.Column
    """
    logo = sg.Image(filename=icon_filepath, background_color=background_color)
    title = sg.Text(title, background_color=background_color, justification='c', font=fonts.TITLE, text_color=colors.TEXT_COLOR_ON_PRIMARY)

    
    if subtitle:
        subtitle = sg.Text(subtitle, background_color=background_color, font=fonts.SUBTITLE, text_color=colors.TEXT_COLOR_ON_PRIMARY, pad=((0, 0), (20, 0)))
    
    bottom_filler = sg.Text(size=(0, 1), background_color=background_color)

    header_elements = [
        [logo],
        [title],
        [separator]
    ]
    
    if subtitle:
        header_elements.append([subtitle])
    header_elements.append([bottom_filler])

    header = sg.Column(layout=header_elements, background_color=background_color, expand_x=True, element_justification='c')

    return header


def build_form(items, top_pad=0, bottom_pad=0, background_color=colors.PRIMARY_LIGHT):
    """Retorna una forma de inputs y botones apilados verticalmente.
    
        Parámetros
        ----------
            inputs_buttons : dict
                De la forma {'inputs': [], 'buttons': []}
    """
    
    form_elements = []

    form_elements.append([sg.Text(size=(0, top_pad), background_color=background_color)])
    
    for i in range(len(items['inputs'])):
        form_elements.append([items['inputs'][i]])
        # separator
        form_elements.append([sg.Text('', size=(0, 1), background_color=background_color)])
 
    for i in range(len(items['buttons'])):
        form_elements.append([items['buttons'][i]])
        # separator
        form_elements.append([sg.Text('', size=(0, 1), background_color=background_color)])

    form_elements.append([sg.Text(size=(0, bottom_pad), background_color=background_color)])

    form_container = sg.Column(layout=form_elements, background_color=background_color, expand_x=True, expand_y=True, element_justification='c')

    return form_container
# TODO crear ventana que pregunte si se quiere registrar!
import PySimpleGUI as sg


import src.globals.colors as colors
import src.globals.texts as texts
import src.globals.sizes as sizes

import src.globals.elements as elements
import src.globals.paths as paths


sg.set_options(
    button_element_size=(30, 2),
)


def build_body():
    gender_input = elements.custom_input(texts.REGISTER_GENDER, '-GENDER-', colors.PRIMARY_LIGHT, colors.TEXT_COLOR_ON_PRIMARY, colors.TEXT_COLOR_ON_PRIMARY, True)
    age_input = elements.custom_input(texts.REGISTER_AGE, '-AGE-', colors.PRIMARY_LIGHT, colors.TEXT_COLOR_ON_PRIMARY, colors.TEXT_COLOR_ON_PRIMARY, False)
    
    register_bttn = elements.custom_button(texts.REGISTER_BTTN, '-REGISTRARSE-', bind_return_key=True)
    back_bttn = elements.custom_button(texts.BACK_BTTN, '-BACK-')
    
    return elements.build_form({'inputs': [gender_input, age_input], 'buttons': [register_bttn, back_bttn]}, 2, 1)
    


def build():
    layout = [
        [elements.exit_bttn_bar(colors.PRIMARY)],
        [elements.header(paths.REGISTER_ICON, colors.PRIMARY, texts.REGISTER_TITLE, elements.separator2(colors.PRIMARY, colors.TEXT_COLOR_ON_PRIMARY))], 
        [build_body()]
    ]
    
    window = sg.Window('', layout=layout, keep_on_top=True, no_titlebar=True, grab_anywhere=True, size=sizes.LOGIN_SIZE)
    
    return window
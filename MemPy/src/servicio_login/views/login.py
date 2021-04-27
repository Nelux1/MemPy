import PySimpleGUI as sg

import src.globals.colors as colors
import src.globals.fonts as fonts
import src.globals.texts as texts
import src.globals.sizes as sizes

import src.globals.elements as elements
import src.globals.paths as paths


def build_body():
    user_input = elements.custom_input(texts.USERNAME_TEXT, '-USERNAME-', colors.PRIMARY_LIGHT, colors.TEXT_COLOR_ON_PRIMARY, colors.TEXT_COLOR_ON_PRIMARY, True)
    login_bttn = elements.custom_button(texts.LOGIN_BTTN, '-LOGIN-', bind_return_key=True)
    return elements.build_form({'inputs': [user_input], 'buttons': [login_bttn]}, 5, 1)


def build_footer():
    footer = sg.Text(text=texts.FOOTER_VALID_USER, justification='center', font=fonts.FOTTER, background_color=colors.PRIMARY_LIGHT, text_color=colors.TEXT_COLOR_ON_PRIMARY)
    
    return sg.Column(layout=[[footer]], background_color=colors.PRIMARY_LIGHT, expand_x=True, expand_y=True, element_justification='c')


def build():
    layout = [
        [elements.exit_bttn_bar(colors.PRIMARY)],
        [elements.header(paths.LOGIN_ICON, colors.PRIMARY,texts.LOGIN_TITLE, elements.separator2(colors.PRIMARY, colors.TEXT_COLOR_ON_PRIMARY), texts.LOGIN_SUBTITLE)],
        [build_body()],
        [build_footer()]
    ]
    
    window = sg.Window('', layout=layout, keep_on_top=True, no_titlebar=True, grab_anywhere=True, size=sizes.LOGIN_SIZE)
    
    return window
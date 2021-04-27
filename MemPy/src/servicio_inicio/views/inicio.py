import PySimpleGUI as sg

import src.globals.colors as colors
import src.globals.fonts as fonts
import src.globals.texts as texts
import src.globals.sizes as sizes

import src.globals.elements as elements
import src.globals.paths as paths


def button(text):   
    return elements.custom_button(text, size=(18, 2), pad=((10, 10), (0, 0)))


def buttons_bar():
    buttons = sg.Column([[button(texts.PLAY_BTTN), button(texts.SCORES_BTTN), button(texts.STATISTICS_BTTN), button(texts.CONFIG_BTTN)]], background_color=colors.PRIMARY_LIGHT)
    buttons_container = sg.Column([[buttons]], background_color=colors.PRIMARY_LIGHT, expand_x=True, element_justification='c')

    return buttons_container


def build():
    layout = [
        [elements.exit_bttn_bar(colors.PRIMARY_LIGHT)],
        [sg.Text('', size=(0, 3), background_color=colors.PRIMARY_LIGHT)],
        [elements.separator1(colors.PRIMARY_LIGHT, colors.TEXT_COLOR_ON_PRIMARY)],
        [elements.header(paths.HOME_ICON, colors.PRIMARY_LIGHT, texts.INITIAL_SCREEN_TITLE, elements.separator2(colors.PRIMARY_LIGHT, colors.TEXT_COLOR_ON_PRIMARY))],
        [sg.Text('', size=(0, 2), background_color=colors.PRIMARY_LIGHT)],
        [buttons_bar()],
        [elements.separator1(colors.PRIMARY_LIGHT, colors.TEXT_COLOR_ON_PRIMARY)]
    ]
    
    window = sg.Window('', layout=layout, no_titlebar=True, keep_on_top=True, grab_anywhere=True, size=sizes.MAIN_SIZE, background_color=colors.PRIMARY_LIGHT, element_justification='c')
    
    return window
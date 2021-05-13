import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import exitbar_widget, separator_widget, option_widget


def build():
    title = sg.Text(
        text='Configuraciones',
        font=('times', 30, 'bold'),
        background_color=colors.PRIMARY_LIGHT,
        text_color=colors.BLACK,
        size=(25, 1),
        justification='c'
    )

    level_select = option_widget.build(
        'Elegir nivel a configurar',
       '-NIVEL-',
        [1, 2, 3],
        1
    )

    config_mensaje = config_option('Mensajes', '-MENSAJES-')
    config_partida = config_option('Partida', '-PARTIDA-')
    config_estilo = config_option('Estilos', '-ESTILO-')

    return sg.Window(
        title='',
        layout=[
            [exitbar_widget.build(colors.PRIMARY_LIGHT)],
            [title],
            [separator_widget.separator2(colors.PRIMARY_LIGHT, colors.BLACK)],
            [level_select],
            [config_mensaje],
            [config_partida],
            [config_estilo],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
        ],
        no_titlebar=True,
        keep_on_top=True,
        grab_anywhere=True,
        element_justification='c',
        background_color=colors.PRIMARY_LIGHT,
        finalize=True
    )


def config_option(text, key):
    return sg.Button(
        button_text=text,
        key=key,
        font=('courier', 16),
        button_color=(colors.WHITE, colors.BLACK),
        mouseover_colors=(colors.BLACK, colors.PRIMARY),
        pad=(0, 10),
    )
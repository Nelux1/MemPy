import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import exitbar_widget, separator_widget, option_widget


def build():
    title = sg.Text(
        text='Configuración de\nmensajes',
        justification='c',
        background_color=colors.PRIMARY_LIGHT,
        text_color=colors.BLACK,
        font=('times', 30, 'bold'),
        size=(25, None)
    )

    victoria = option_widget.build(
        'Mensaje de Victoria', 
        '-WIN_MESSAGE-',
        ['¡Ganaste!', '¡Victoria!', '¡No estuvo mal!', '¡Muy bien!', '¡Lo lograste!'],
        '¡Ganaste!',
    )

    derrota = option_widget.build(
        'Mensaje de Derrota',
        '-LOSS_MESSAGE-',
        ['¡Perdiste!', '¡Derrota!', 'Casi... pero ¡perdiste!', '¡Mejor suerte para la próxima!', '¡A seguir intentando!'],
        '¡Perdiste!',
    )

    restante = option_widget.build(
        'Mensaje del Tiempo Restante',
        '-TIMELEFT_MESSAGE-',
        ['¡Quedan {} segundos!', 'Tiempo restante: {}', 'Faltan {} segundos para terminar', '¡Mira el tiempo que perdiste! {}'],
        '¡Quedan {} segundos!',
    )

    guardar = sg.Button(
        button_text='Guardar',
        key='-GUARDAR-',
        font=('courier', 13),
        size=(25, 3)
    )

    mid_sep = sg.Text(background_color=colors.PRIMARY_LIGHT, size=(1, None))

    cancelar = sg.Button(
        button_text='Cancelar',
        key='-CANCELAR-',
        font=('courier', 13),
        size=(25, 3)
    )

    return sg.Window(
        title='',
        layout=[
            [exitbar_widget.build(colors.PRIMARY_LIGHT)],
            [title],
            [separator_widget.separator2(colors.PRIMARY_LIGHT, colors.BLACK)],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
            [victoria],
            [derrota],
            [restante],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
            [guardar, mid_sep, cancelar],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 2)],
        ],
        no_titlebar=True,
        keep_on_top=True,
        grab_anywhere=True,
        background_color=colors.PRIMARY_LIGHT,
        element_justification='c',
        finalize=True
    )

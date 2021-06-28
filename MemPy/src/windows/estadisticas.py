import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import exitbar_widget, separator_widget


def build():
    title = sg.Text(
        text='ESTADÍSTICAS',
        font=('times', 30, 'bold'),
        background_color=colors.PRIMARY_DARK,
        text_color=colors.WHITE,
        size=(25, 1),
        justification='c'
    )

    return sg.Window(
        title='MemPy',
        layout=[
            [exitbar_widget.build(colors.PRIMARY_DARK)],
            [title],
            [option_button('Top 10 palabras', '-TOP-')],
            [option_button('Partidas por estado', '-PARTIDA-')],
            [option_button('Finalizadas por genero', '-GENERO-')],
            [option_button('Volver', '-BACK-')],
            [separator_widget.invisible_horizontal(colors.BACKGROUND, 2)],
        ],
        no_titlebar=True,
        keep_on_top=True,
        element_justification='c',
        background_color=colors.BACKGROUND,
        finalize=True
    )

def option_button(text, key):
    """Botones utilizados unicamente por esta ventana."""
    return sg.Button(
        button_text=text,
        key=key,
        font=('courier', 16),
        button_color=(colors.WHITE, colors.BLACK),
        pad=(0, 10),
    )

     
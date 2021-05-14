import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import exitbar_widget, separator_widget


def build():
    title = sg.Text(
        text='ESTADÍSTICAS',
        font=('times', 30, 'bold'),
        background_color=colors.PRIMARY_LIGHT,
        text_color=colors.WHITE,
        size=(25, 1),
        justification='c'
    )

    return sg.Window(
        title='MemPy',
        layout=[
            [exitbar_widget.build(colors.PRIMARY_DARK)],
            [title],
            [separator_widget.estilo2(colors.PRIMARY_LIGHT, colors.WHITE)],
        ],
        background_color=colors.PRIMARY_LIGHT,
        no_titlebar=True,
        element_justification='c',
        keep_on_top=True,
        finalize=True
    )
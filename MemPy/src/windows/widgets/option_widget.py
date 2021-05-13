import PySimpleGUI as sg

from src.windows import colors
from src.windows.widgets import separator_widget


def build(text, key, values, default):
    label = sg.Text(
        text=text,
        text_color=colors.BLACK,
        font=('times', 18),
        background_color=colors.PRIMARY_LIGHT
    )

    combo = custom_combo(values, default, key)

    return sg.Column(
        layout=[
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 1)],
            [label],
            [combo],
            [separator_widget.invisible_horizontal(colors.PRIMARY_LIGHT, 1)]
        ],
        element_justification='c',
        background_color=colors.PRIMARY_LIGHT
    )
    

def custom_combo(values, default, key):
    return sg.Combo(
        key=key,
        values=values,
        default_value=default,
        background_color=colors.WHITE,
        font=('courier', 15),
        auto_size_text=False,
        size=(35, None),
        text_color=colors.BLACK,
        readonly=True
    )


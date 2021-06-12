import PySimpleGUI as sg
from src.windows import colors
from src.windows.widgets import exitbar_widget
from src.components.posiciones import posiciones
import random
import string

def build(username,puntaje):
        def word():
         return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        def number(max_val=1000):
            return random.randint(0, max_val)

        def make_table(num_rows, num_cols):
            data = [[j for j in range(num_cols)] for i in range(num_rows)]
            data[0] = [word() for __ in range(num_cols)]
            for i in range(1, num_rows):
                data[i] = [word(), *[number() for i in range(num_cols - 1)]]
            return data

        # ------ Make the Table Data ------
        data = make_table(num_rows=15, num_cols=6)
        headings = [str(data[0][x])+'     ..' for x in range(len(data[0]))]

        # ------ Window Layout ------
        return sg.Window(
            title='Puntajes',
            layout = [
            [sg.Table(values=data[1:][:], headings=headings, max_col_width=25,
                            # background_color='light blue',
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='right',
                            num_rows=10,
                            alternating_row_color='lightyellow',
                            key='-TABLE-',
                            row_height=10,
                            tooltip='POSICIONES')]
                ]
        )            
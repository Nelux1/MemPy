import PySimpleGUI as sg
from src.windows import colors
from src.windows.widgets import exitbar_widget
import os
import csv
import pandas as pd

archivo=os.path.join(os.getcwd(),'posiciones.csv')


def build(username,puntaje):
    data = []
    header_list = []
    archivo_csv=open(archivo,"r")
    df = pd.read_csv(archivo_csv, sep=',')
    df = df.sort_values('PUNTOS',ascending=False)
    data = df.values.tolist()               
    header_list = df.iloc[0].tolist()
    data = df[0:].values.tolist()
    with open(archivo, "r") as file:
         reader = csv.reader(file)
         header_list = next(reader)  
    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  header_text_color=colors.BLACK,
                            header_background_color=colors.PRIMARY_DARK,
                            header_font=('Courier',30),
                            max_col_width=25,
                            pad=(5,5),
                            auto_size_columns=False,
                            row_height=50,
                            font=('Courier',30),
                            justification='right',
                            alternating_row_color=colors.PRIMARY_LIGHT,
                            background_color=colors.BACKGROUND,
                            text_color=colors.BLACK,
                            num_rows=min(50, 50))]]
    
    return sg.Window('POSICIONES', layout, grab_anywhere=False,size=(500,300))

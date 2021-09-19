import pandas as pd
import os
import csv
from src.windows import colors
import PySimpleGUI as sg

archivo = os.path.join("datos_estadisticos.csv")

def build():
    data = []
    header_list = []
    archivo_csv=open(archivo,"r")
    df = pd.read_csv(archivo_csv, sep=',')
    palabras_ok = [df["Estado"]== "ok"]
    df = palabras_ok.groupby(["Palabra"]["Estado"]).count().sort_values(ascending=False).head(10)
    data = df.values.tolist()               
    header_list = df.iloc[0].tolist()
    data = df[0:].values.tolist()
    with open(archivo, "r") as file:
         reader = csv.reader(file)
         header_list = next(reader)  
    layout = [
        [sg.Table(values= data,
                  headings= header_list,
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
    
    return sg.Window('TOP 10', layout, grab_anywhere=False,size=(500,500))
import pandas as pd
import os
from matplotlib import pyplot as plt

datos_path = os.path.join("datos_estadisticos.csv")
data_set = pd.read_csv(datos_path)

def top_10_palabras():
    palabras_ok = data_set[data_set["Estado"]== "ok"]
    top_10= palabras_ok.groupby(["Palabra"])["Estado"].count().sort_values(ascending=False).head(10)
    return top_10

def porcentaje_por_estado():
    datos= data_set.groupby(["Nombre de evento"])["Nombre de evento"].count()
    datos= datos.drop(["Inicio_partida","intento"], axis=0)
    etiquetas= 'Abandonadas','Canceladas', 'Finalizadas'
    explosion = (0,0,0.1)
    colores=['red','orange','green']
    plt.pie(datos,labels= etiquetas,shadow='true', autopct="%1.1f%%",explode=explosion,colors=colores)
    plt.axis('equal')
    plt.legend(title="Estados de partidas", loc= 'lower right')
    plt.show()
    return

def porcentaje_fin_genero():
    partidas_finalizadas= data_set[data_set["Estado"]=="finalizada"]
    finalizadas_gen= partidas_finalizadas.groupby(["usuarie -genero"])["usuarie -genero"].count()
    etiquetas = finalizadas_gen.index.tolist()
    colores = ['blue','pink']
    plt.pie(finalizadas_gen,labels=etiquetas,shadow='true,', autopct='%1.1f%%', colors= colores)
    plt.axis('equal')
    plt.legend(title='Partidas finalizadas por genero', loc= 'lower right')
    plt.show()
    return 

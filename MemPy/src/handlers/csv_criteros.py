import os.path
import os
import csv
import datetime

path_csv = os.path.join(os.getcwd(), "steam.csv")

#Separar en una lista los valores que tienen mas de un parametro(?)
with open(path_csv, "r", encoding="utf-8") as archivo_steam:
    data_net = csv.reader(archivo_steam, delimiter= ',')
    datos = data_net
    lista_dict = []
    for i in csv.DictReader(archivo_steam):
        lista_dict.append(dict(i))
    
#configuraciones de datetime
nro_dia = datetime.datetime.today().weekday()
dias_semana =['lunes',',martes','miercoles','jueves','viernes','sabado','domingo']
mañana, tarde =[(0,12), (13,23)]
criterios_data = {}

for dia in dias_semana:
    criterios_data[dia] = {mañana: {}, tarde: {}}
print(criterios_data)

def get_nombre_publisher(publicador, desarrollador):
    data_juego = list(filter(lambda x : (x['publisher']== publicador and x['developer']=='desarrollador'),lista_dict))
    return list(lambda nom: nom['name'], data_juego)

criterios_data['lunes'][mañana]={'criterio':'Nombres de juegos desarrollados y publicados por Valve', 
                                'funcion': get_nombre_publisher, 'params': ('Valve','Valve')}


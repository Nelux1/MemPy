import os.path
import os
import csv
import datetime


path_steam_csv = os.path.join(os.getcwd(), "steam.csv")
path_tv_csv = os.path.join(os.getcwd(), 'TV_Shows.csv')
path_disney_csv = os.path.join(os.getcwd(),'disney_movies.csv')
path_music_csv = os.path.join(os.getcwd(),'spotify-2000.csv')


#Separa en una lista de diccionarios con las claves siendo las categorias, y los valores lo que respresentan
with open(path_steam_csv, "r", encoding="utf-8") as archivo_steam:
    data_net = csv.reader(archivo_steam, delimiter= ',')
    datos = data_net
    dicc_steam = []
    for i in csv.DictReader(archivo_steam):
        dicc_steam.append(dict(i))

with open(path_tv_csv, "r", encoding="utf-8") as archivo_tv:
    data_net = csv.reader(archivo_tv, delimiter =',')
    datos = data_net
    dicc_tv = []
    for i in csv.DictReader(archivo_tv):
        dicc_tv.append(dict(i))

with open(path_disney_csv, "r", encoding="utf-8") as archivo_disney:
    data_net = csv.reader(archivo_disney, delimiter =',')
    datos = data_net
    dicc_disney = []
    for i in csv.DictReader(archivo_disney):
        dicc_disney.append(dict(i))

with open(path_music_csv, "r", encoding="utf-8") as archivo_musica:
    data_net = csv.reader(archivo_musica, delimiter =',')
    datos = data_net
    dicc_musica = []
    for i in csv.DictReader(archivo_musica):
        dicc_musica.append(dict(i))

for r in dicc_tv:
    if r['IMDb'] == '':
        r['IMDb'] = '0'


#configuraciones de datetime
nro_dia = datetime.datetime.today().weekday()
dias_semana =['lunes',',martes','miercoles','jueves','viernes','sabado','domingo']
madrugada, mañana, tarde, noche =[(0,6),(7,12),(13,18),(19,23)]
criterios_data = {}

for dia in dias_semana:
    criterios_data[dia] = {madrugada: {}, mañana: {}, tarde: {}, noche: {}}


#Estructuras de las funciones para encontrar los datos solicitados en el diccionario
def get_juego_con_publisher_developer(publicador, desarrollador):
    data_juego = list(filter(lambda x : (x['publisher']== publicador and x['developer']==desarrollador),dicc_steam))
    return list(map(lambda nom: nom['name'], data_juego))

def get_developer_con_genero_precio_positivos(genero, precio, positivos):
    data_juego = list(filter(lambda x : (x['genres']== genero and float(x['price'])<=precio and int(x['positive_ratings'])>= positivos),dicc_steam))
    return set(list(map(lambda nom: nom['developer'], data_juego)))

def get_cancion_con_artista_año(artista, años):
    data_juego = list(filter(lambda x : (x['Artist']== artista and int(x['Year']) in años),dicc_musica))
    return list(map(lambda nom: nom['Title'], data_juego))

def get_artista_con_genero_año_popularidad(genero, años, popularidad):
    data_juego = list(filter(lambda x : (x['Top Genre']== genero and int(x['Year']) in años and int(x['Popularity']) >= popularidad),dicc_musica))
    return list(set(map(lambda nom: nom['Artist'], data_juego)))

def get_pelicula_con_genero_edad(genero, edad):
    data_juego = list(filter(lambda x : (x['genre']== genero and x['mpaa_rating']==edad),dicc_disney))
    return list(map(lambda nom: nom['movie_title'], data_juego))

def get_pelicula_con_dinero_genero(genero, dinero):
    data_juego = list(filter(lambda x : (x['genre']== genero and int(x['total_gross'])>=dinero),dicc_disney))
    return list(map(lambda nom: nom['movie_title'], data_juego))

def get_serie_con_netflix_IMDb_año(r_IMDb, año):
    data_juego = list(filter(lambda x : (x['Netflix']== '1' and x['Year']== año and float(x['IMDb']) >= r_IMDb),dicc_tv))
    return list(map(lambda nom: nom['Title'], data_juego))

def get_serie_con_Amazon_edad_año(edad, año):
    data_juego = list(filter(lambda x : (x['Prime Video']== '1' and x['Year']== año and x['Age'] == edad),dicc_tv))
    return list(map(lambda nom: nom['Title'], data_juego))

criterios_data['lunes'] = {
    madrugada: {
        'criterio':'Nombres de juegos desarrollados y publicados por Valve', 
        'función': get_juego_con_publisher_developer,
        'parametros': ('Valve','Valve')
    },
    mañana: {
        'criterio':'Nombres de las canciones mas populares de Coldplay del año de 2000 hasta 2009', 
        'función': get_cancion_con_artista_año,
        'parametros': ('Coldplay',list(range(2000,2010,1)))
    },
    tarde: {
        'criterio':'Nombres de peliculas de Disney en genero musical para todas las edades', 
        'función': get_pelicula_con_genero_edad,
        'parametros': ('Musical','G')
    },
    noche: {
        'criterio':'Nombres de las series de Netflix, estrenadas en el año 2015 con nota de IMDb mayor a 8', 
        'función': get_serie_con_netflix_IMDb_año,
        'parametros': (8,'2015')
    }
}
criterios_data['martes']= {
    madrugada:{
        'criterio':'Nombres de los artistas con popularidad mayor o igual a 30 en la categoria de dance pop, en los años de 2010 hasta 2019', 
        'función': get_artista_con_genero_año_popularidad,
        'parametros': ('dance pop',list(range(2010,2020,1)),30)
    },
    mañana:{
        'criterio':'Nombres de desarrolladoras con juegos del genero de acción, menores a $10 de precio, y mas de 1000 positivos', 
        'función': get_developer_con_genero_precio_positivos,
        'parametros': ('Action',10,1000)
    },
    tarde:{
        'criterio':'Nombres de las series de Prime Video que se estrenaron en 2019 y son para mayores de 18 años', 
        'función': get_serie_con_Amazon_edad_año,
        'parametros': ('18+','2019')
    },
    noche:{
        'criterio':'Nombres de peliculas de Disney en el genero de comedia, que produjeron mas de $70000000', 
        'función': get_pelicula_con_dinero_genero,
        'parametros': ('Comedy',70000000)
    }
}
criterios_data['miercoles']= {
    madrugada:{
        'criterio':'Nombres de las series de Prime Video que se estrenaron en 2018 y son para mayores de 16 años', 
        'función': get_serie_con_Amazon_edad_año,
        'parametros': ('16+','2018')
    },
    mañana: {
        'criterio':'Nombres de desarrolladoras con juegos del genero RPG menores a $30 de precio, y mas de 5000 positivos', 
        'función': get_developer_con_genero_precio_positivos,
        'parametros': ('RPG',30,10000)
    },
    tarde: {
        'criterio':'Nombres de los artistas con popularidad mayor a 40 en la categoria de album rock, en los años de 2000 hasta 2014', 
        'función': get_artista_con_genero_año_popularidad,
        'parametros': ('album rock',list(range(2000,2015,1)),50)
    },
    noche:{
        'criterio':'Nombres de peliculas de Disney en el genero de aventura, que produjeron mas de $100000000', 
        'función': get_pelicula_con_dinero_genero,
        'parametros': ('Adventure',100000000)
    }
}
criterios_data['jueves']={
    madrugada:{
        'criterio':'Nombres de las canciones mas populares de los Rolling Stones del año 1969 hasta 1980', 
        'función': get_cancion_con_artista_año,
        'parametros': ('The Rolling Stones',list(range(1969,1981,1)))
    },
    mañana:{
        'criterio':'Nombres de las series de Netflix, estrenadas en el año 2018 con nota de IMDb mayor a 7', 
        'función': get_serie_con_netflix_IMDb_año,
        'parametros': (7,'2018')
    },
    tarde:{
        'criterio':'Nombres de peliculas de Disney en genero drama para mayores de 13', 
        'función': get_pelicula_con_genero_edad,
        'parametros': ('Drama','PG-13')
    },
    noche: {
        'criterio':'Nombres de juegos desarrollados por Bethesda Game Studios y publicados por Bethesda Softworks', 
        'función': get_juego_con_publisher_developer,
        'parametros': ('Bethesda Softworks','Bethesda Game Studios')
    }
}


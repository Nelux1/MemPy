"""manipulacion de funciones de configuraciones"""

          
def tiempos(t,nivel):
 minutos=0   
 if t[nivel]["-TIEMPO_MIN-"] == "1 minuto":
     minutos= 60
 elif t[nivel]["-TIEMPO_MIN-"] == "2 minutos":
     minutos= 120
 elif t[nivel]["-TIEMPO_MIN-"] == "3 minutos":
     minutos= 180
 elif t[nivel]["-TIEMPO_MIN-"] == "5 minutos":
     minutos= 300
 elif t[nivel]["-TIEMPO_MIN-"] == "1:30 minutos":
     minutos= 90     
 return minutos

def cuadros(c,nivel):
 if c[nivel]["-CASILLAS-"] == '6x6': 
   casilla=6
 elif c[nivel]["-CASILLAS-"] == '8x8':
   casilla=8
 elif c[nivel]["-CASILLAS-"] == '10x10':
   casilla=10
 return casilla


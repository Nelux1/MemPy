"""manipulacion de funciones del juego con las configuraciones del mismo"""




def pistas(p,n):
  if p[n]["-PISTAS-"]== True:
   pista=True
  else:
   pista=False
  return pista   
          
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
 if c[nivel]["-CASILLAS-"] == '4x2': 
   casilla=2
 elif c[nivel]["-CASILLAS-"] == '4x3':
   casilla=3
 elif c[nivel]["-CASILLAS-"] == '4x4':
   casilla=4
 return casilla

def mensajes (m,nivel):
  mensaje=''
  if m[nivel]["-TIMELEFT_MESSAGE-"] == "¡Quedan pocos segundos!":
    mensaje="¡Quedan pocos segundos!"
  if m[nivel]["-TIMELEFT_MESSAGE-"] == "Se te termina el tiempo!":
    mensaje="Se te termina el tiempo!"
  if m[nivel]["-TIMELEFT_MESSAGE-"] == "toca cualquier ficha rapido!!":
    mensaje="toca cualquier ficha rapido!!"
  if m[nivel]["-TIMELEFT_MESSAGE-"] == "¡Mira el tiempo que perdiste!":      
    mensaje="¡Mira el tiempo que perdiste!"
  return mensaje  

def can_palabras_adivinar(palab):
  cant=0
  if palab == 2:
    cant= 4
  if palab == 3:
    cant= 6
  if palab == 4: 
    cant= 8
  return cant 
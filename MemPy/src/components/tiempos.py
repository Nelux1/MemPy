

def tiempos(t):
 if t[0]["-TIEMPO_MIN-"] == "1 minutos":
     minutos= 60
 elif t[0]["-TIEMPO_MIN-"] == "2 minutos":
     minutos= 120
 elif t[0]["-TIEMPO_MIN-"] == "3 minutos":
     minutos= 180
 elif t[0]["-TIEMPO_MIN-"] == "5 minutos":
     minutos= 300
 elif t[0]["-TIEMPO_MIN-"] == "1:30 minutos":
     minutos= 90    
 return minutos


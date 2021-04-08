"""Funciones para configurar los valores de inicio/fin para un reporte."""
from consolemenu.validators.base import BaseValidator


# un validator para los números
class ValidatorNumero(BaseValidator):
    """Clase para verificar que un input sea un número positivo."""
    
    def __init__(self):
        super().__init__()
        
    def validate(self, input_string):
        try:
            numero = int(input_string)
            
            if numero >= 0:
                return True
        except:
            pass
        
        return False
    

def obtener_numero(indice, mensaje, lista):
    """Lee un número (mostrando el mensaje) y lo guarda en lista[indice]."""
    lista[indice] = leer_numero_valido(mensaje)

    return lista
      
        
def leer_numero_valido(mensaje):
    """Retorna un número válido.
    
        Válido -> un número positivo.
        Pide input al usuario hasta que es válido.
    """
    from . import utilidades

    resultado_lectura = utilidades.input(prompt=mensaje, validators=[ValidatorNumero()])
    
    while not resultado_lectura.validation_result:
        utilidades.println(f'El valor ingresado es inválido. Por favor, intente nuevamente.')
        resultado_lectura = utilidades.input(prompt=mensaje, validators=[ValidatorNumero()])
        
    return int(resultado_lectura.input_string)

"""Funciones para configurar los valores de inicio/fin para un reporte."""
from consolemenu.validators.base import BaseValidator

def iniciar_configuracion(tipo):
    """Abre el menú de configuración para el reporte."""
    # abre el menú de configuración enviándole el tipo de reporte
    from menus.menu_configurar_reporte import crear_menu_configurar_reporte
    crear_menu_configurar_reporte(tipo).show()


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
    """Lee un número (mostrando el mensaje) y lo guarda en lista[indice].
    
        La lista que recibe proviene del menú. El menú guarda los resultados
        en base al return de las funciones que llama, por eso no basta
        sólo con modificarla.
    """
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

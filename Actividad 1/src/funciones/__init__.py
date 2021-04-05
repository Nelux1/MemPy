"""Contiene variables globales para todas las funciones."""
from consolemenu import PromptUtils
from menus import VENTANA_PRINCIPAL

# se usa para interactuar con el usuario. (e/s)
utilidades = PromptUtils(VENTANA_PRINCIPAL)

# se muestra al usuario luego de mostrar algo en consola
# es necesario usarlo para que no se re-abran los menús dsp de imprimir algo!
MENSAJE_PARA_CONTINUAR = 'Presione [Enter] para continuar'
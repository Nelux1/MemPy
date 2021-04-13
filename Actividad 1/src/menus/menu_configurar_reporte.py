from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

from . import VENTANA_PRINCIPAL, MENSAJE_VOLVER_ATRAS
from funciones.funciones_configurar_reporte import obtener_numero
from funciones.funciones_reporte import generar_e_imprimir_reporte

# pseudo constantes -> texto del menu_configurar_reporte
TITULO_CONFIGURAR = 'Elección de rango del reporte'
PROLOGO_CONFIGURAR = f'Indique el rango de notas sobre el cual realizar el reporte \N{maple leaf}\n\nSi ambos valores del rango son iguales, sólo se incluirán las personas con ese valor específico!\n'

# pseudo constantes -> texto de los ítems del menú
TEXTO_ITEM_VALOR_INICIO = 'Elegir el valor de comienzo del reporte'
TEXTO_ITEM_VALOR_FIN = 'Elegir el valor de fin del reporte'
TEXTO_ITEM_REALIZAR = 'Guardar y realizar el reporte'


def crear_menu_configurar_reporte(tipo):
    """Crea el menú pensando para utilizar junto a menu_reportes.
    
        El menú tiene que retener los valores del rango y el tipo,
        hasta que se seleccione la opción de realizar.
    """    

    menu = ConsoleMenu(
        title=TITULO_CONFIGURAR,
        screen=VENTANA_PRINCIPAL,
        prologue_text=PROLOGO_CONFIGURAR,
        exit_option_text=MENSAJE_VOLVER_ATRAS
    )

    
    # para guardar los datos que recolecta
    menu.returned_value = [0, 0]
    
    menu.append_item(FunctionItem(TEXTO_ITEM_VALOR_INICIO, function=obtener_numero, args=[0, 'Indicar valor de comienzo: ', menu.returned_value]))
    menu.append_item(FunctionItem(TEXTO_ITEM_VALOR_FIN, function=obtener_numero, args=[1, 'Indicar valor de fin: ', menu.returned_value]))

    menu.append_item(FunctionItem(TEXTO_ITEM_REALIZAR, function=generar_e_imprimir_reporte, args=[tipo, menu.returned_value], should_exit=True))
    
    return menu
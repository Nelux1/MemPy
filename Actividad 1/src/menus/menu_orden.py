from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem


# pseudo constantes -> texto del menú orden
TITULO_ORDEN = f'¿En base a qué criterio desea ordenar los datos? \N{beverage box}'
PROLOGO_ORDEN = 'Luego de su elección, le mostraremos una lista con todos los datos de los alumnos ordenados por el criterio elegido.'

# pseudo constantes -> texto de los ítems del menú orden
TEXTO_ITEM_ORDEN_NOMBRES = 'Ordenar en base a los nombres'
TEXTO_ITEM_ORDEN_EVAL1 = 'Ordenar en base a las notas de la 1er evaluación'
TEXTO_ITEM_ORDEN_EVAL2 = 'Ordenar en base a las notas de la 2da evaluación'
TEXTO_ITEM_ORDEN_FINAL = 'Ordenar en base a la nota final'


def crear_menu_orden():
    """Crea un menú pensando para el proceso de ordenar/visualizar los datos."""

    from . import VENTANA_PRINCIPAL, MENSAJE_VOLVER_ATRAS

    menu = ConsoleMenu(
        title=TITULO_ORDEN,
        prologue_text=PROLOGO_ORDEN,
        screen=VENTANA_PRINCIPAL,
        exit_option_text=MENSAJE_VOLVER_ATRAS
    )

    from funciones.funciones_orden import imprimir_alumnos, ordenar_por_clave, ordenar_por_evaluacion
    
    menu.append_item(FunctionItem(TEXTO_ITEM_ORDEN_NOMBRES, imprimir_alumnos, [ordenar_por_clave('nombre')]))
    menu.append_item(FunctionItem(TEXTO_ITEM_ORDEN_EVAL1, imprimir_alumnos, [ordenar_por_evaluacion(1)]))
    menu.append_item(FunctionItem(TEXTO_ITEM_ORDEN_EVAL2, imprimir_alumnos, [ordenar_por_evaluacion(2)]))
    menu.append_item(FunctionItem(TEXTO_ITEM_ORDEN_FINAL, imprimir_alumnos, [ordenar_por_clave('nota_final')]))

    return menu

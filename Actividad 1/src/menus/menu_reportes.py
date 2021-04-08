from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem


# pseudo constantes -> texto del menú reportes
TITULO_REPORTES = f'¿Sobre qué desea realizar el reporte? \N{fallen leaf}'
PROLOGO_REPORTES = f'\N{maple leaf}Luego de su elección, le pediremos que ingrese un rango (de notas), en base al cuál retornaremos los nombres de quienes estén dentro del mismo.'

# pseudo constantes -> texto en los ítems del menú reportes
TEXTO_ITEM_REPORTE_EVAL1 = 'Reporte sobre los resultados de la evaluación 1'
TEXTO_ITEM_REPORTE_EVAL2 = 'Reporte sobre los resultados de la evaluación 2'
TEXTO_ITEM_REPORTE_FINAL = 'Reporte sobre la nota final'


def crear_menu_reportes():
    """Crea el menú pensando para el proceso de crear un reporte."""

    from . import VENTANA_PRINCIPAL, MENSAJE_VOLVER_ATRAS

    menu = ConsoleMenu(
        title=TITULO_REPORTES,
        screen=VENTANA_PRINCIPAL,
        prologue_text=PROLOGO_REPORTES,
        exit_option_text=MENSAJE_VOLVER_ATRAS
    )

    from funciones.funciones_reporte import iniciar_configuracion

    menu.append_item(FunctionItem(TEXTO_ITEM_REPORTE_EVAL1, iniciar_configuracion, [1]))
    menu.append_item(FunctionItem(TEXTO_ITEM_REPORTE_EVAL2, iniciar_configuracion, [2]))
    menu.append_item(FunctionItem(TEXTO_ITEM_REPORTE_FINAL, iniciar_configuracion, ['nota_final']))
    
    return menu
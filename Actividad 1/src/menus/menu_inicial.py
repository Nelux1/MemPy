from consolemenu import ConsoleMenu
from consolemenu.items import SubmenuItem, FunctionItem


# pseudo_constantes -> texto del menú principal
TITULO_INICIO = f'¡Bienvenido a la actividad 1 \N{snake}!'
SUBTITULO_INICIO = 'Una actividad de procesamiento de datos.'
PROLOGO_INICIO = f'¿Qué operación desea realizar? (Escriba un número de los que se presentan en pantalla y presione [Enter])'
EPILOGO_INICIO = f'\N{broccoli} !ATENCIÓN! \N{broccoli} Si utiliza Windows es probable que cmd no muestre los símbolos utilizados. Mi recomendación es obtener \'Windows Terminal\' desde MS Store para poder verlos! (o alguna otra consola que permita este tipo de carácteres)'
MENSAJE_SALIDA_PROGRAMA = f'Salir del programa \N{door}'

# pseudo constantes -> texto en los ítems del menú principal
TEXTO_ITEM_PROMEDIO = 'Obtener promedio de las notas finales'
TEXTO_ITEM_REPORTE = 'Realizar un reporte sobre los datos de los alumnos'
TEXTO_ITEM_ORDENAR = 'Ordenar y visualizar los datos de los alumnos'


def crear_menu_inicial():
    """Crea el menú pensando para mostrarse al principio del programa."""

    from menus import VENTANA_PRINCIPAL

    menu = ConsoleMenu(
        title=TITULO_INICIO, 
        subtitle=SUBTITULO_INICIO,
        screen=VENTANA_PRINCIPAL,
        prologue_text=PROLOGO_INICIO,
        epilogue_text=EPILOGO_INICIO,
        exit_option_text=MENSAJE_SALIDA_PROGRAMA
    )

    from funciones.funciones_promedio import imprimir_promedio # TODO implementar la función 'imprimir_promedio'
    from .menu_reportes import crear_menu_reportes
    from .menu_orden import crear_menu_orden

    menu.append_item(FunctionItem(TEXTO_ITEM_PROMEDIO, imprimir_promedio))
    menu.append_item(SubmenuItem(TEXTO_ITEM_REPORTE, submenu=crear_menu_reportes(), menu=menu))
    menu.append_item(SubmenuItem(TEXTO_ITEM_ORDENAR, submenu=crear_menu_orden(), menu=menu))

    return menu

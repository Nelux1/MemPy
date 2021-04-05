from . import utilidades, MENSAJE_PARA_CONTINUAR


def imprimir_reporte(tipo):
    """Imprime en consola los resultados del reporte."""
    utilidades.enter_to_continue(MENSAJE_PARA_CONTINUAR)


# pseudo constantes -> textos para la pantalla al obtener rango del reporte.
TEXTO_RANGO_INDICACIONES = f'Indique el rango de notas sobre el cual realizar el reporte \N{maple leaf}\n\nSi ambos valores del rango son iguales, sólo se incluirán las personas con ese valor específico!\n'
TEXTO_RANGO_INVALIDO = f'\N{cross mark} Por favor, especifique un rango numérico válido. INICIO >= FIN y ambos deben ser >= 0\n'
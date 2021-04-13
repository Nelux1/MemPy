from datos.datos import lista_alumnos
from . import utilidades, MENSAJE_PARA_CONTINUAR

#  mensaje que se muestra si el rango para hacer el reporte no es válido.
TEXTO_RANGO_INVALIDO = f'\N{cross mark} No pudo realizarse el reporte. Por favor, especifique un rango numérico válido. FIN >= INICIO\n'
    

def realizar_reporte_nota_final(inicio, fin):
    return list(filter(lambda alumno: alumno['nota_final'] >= inicio and alumno['nota_final'] <= fin, lista_alumnos))


def realizar_reporte_eval(numero, inicio, fin):
    return list(filter(lambda alumno: alumno['notas'][numero] >= inicio and alumno['notas'][numero] <= fin, lista_alumnos))


def realizar_reporte(tipo, inicio, fin):
    """Retorna lista de nombres de quienes entran en el reporte.
    
        Return:
            reporte : dict
                {'tipo': tipo, 'rango': (inicio, fin), 'nombres': []/None}

        Si el reporte es inválido -> 'nombres' == None
    """
    reporte = {'tipo': tipo, 'rango': (inicio, fin), 'nombres': None}
    
    if inicio <= fin:
        if isinstance(tipo, int):
            reporte['nombres'] = realizar_reporte_eval(tipo, inicio, fin)
        else:
            reporte['nombres'] = realizar_reporte_nota_final(inicio, fin)
 
    return reporte


def tipo_str(tipo):
    """Retorna una versión legible del tipo de reporte."""
    if tipo == 'nota_final':
        return 'nota final'
    
    return f'evaluación {tipo + 1}'


def imprimir_reporte(tipo, rango):
    """Imprime en consola los resultados de un reporte.

        Antes de imprimir, debe realizar el reporte.

        Antes de imprimir, verifica que el reporte sea válido.
        (La lista de nombres exista).
    """
    reporte = realizar_reporte(tipo, *rango)

    utilidades.println(f'Reporte sobre {tipo_str(reporte["tipo"])}, en el rango {reporte["rango"]}\n{"-" * 50}\n')

    if reporte['nombres'] is not None:
        if not reporte['nombres']:
            utilidades.println('No entraron alumnos en el reporte.')

        # imprimo en 2 columnas
        for i in range(1, len(reporte['nombres'])):
            utilidades.println(f'{reporte["nombres"][i - 1]["nombre"]:<15}{reporte["nombres"][i]["nombre"]}')
    else:
        utilidades.println(TEXTO_RANGO_INVALIDO)

    utilidades.println()
        
    utilidades.enter_to_continue(MENSAJE_PARA_CONTINUAR)
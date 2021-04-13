from datos.datos import lista_alumnos
from . import utilidades, MENSAJE_PARA_CONTINUAR

#  mensaje que se muestra si el rango para hacer el reporte no es válido.
TEXTO_RANGO_INVALIDO = f'\N{cross mark} No pudo realizarse el reporte. Por favor, especifique un rango numérico válido. FIN >= INICIO\n'
    

# ----- funciones para la lógica de creación de un reporte -----

def filtrar_nota_final(inicio, fin):
    """Retorna iterador de alumnos con nota final entre inicio y fin."""
    return filter(lambda alumno: alumno['nota_final'] >= inicio and alumno['nota_final'] <= fin, lista_alumnos)


def filtrar_eval(numero, inicio, fin):
    """Retorna iterador de alumnos con nota en la evaluación (numero) entre inicio y fin."""
    return filter(lambda alumno: alumno['notas'][numero] >= inicio and alumno['notas'][numero] <= fin, lista_alumnos)


def filtrar_datos(tipo, inicio, fin):
    """Filtra los datos de los alumnos según el tipo."""
    return filtrar_eval(tipo, inicio, fin) if isinstance(tipo, int) else filtrar_nota_final(inicio, fin)


def realizar_reporte(tipo, inicio, fin):
    """Retorna lista de nombres de quienes entran en el reporte.
    
        Return:
            reporte : dict
                {'tipo': tipo, 'rango': (inicio, fin), 'nombres': []}
                
        Si el reporte es inválido -> 'nombres' no existe.
        Reporte inválido == inicio > fin.
    """
    reporte = {'tipo': tipo, 'rango': (inicio, fin)}
    
    if inicio <= fin:
        reporte['nombres'] = list(filtrar_datos(tipo, inicio, fin))

    return reporte


# ----- funciones para la lógica de impresión de un reporte -----

def tipo_str(tipo):
    """Retorna una versión legible del tipo de reporte."""
    if tipo == 'nota_final':
        return 'nota final'
    
    return f'evaluación {tipo + 1}'


def imprimir_reporte(reporte):
    """Imprime en consola los resultados de un reporte.
    
        El reporte puede estar vacío.
    """
    utilidades.println(f'Reporte sobre {tipo_str(reporte["tipo"])}, en el rango {reporte["rango"]}\n{"-" * 50}\n')

    if not reporte['nombres']:
        utilidades.println('No entraron alumnos en el reporte.')

    for i in range(len(reporte['nombres'])):
        utilidades.println(f'{reporte["nombres"][i]["nombre"]:<15}')        
    
    
# ----- función llamada por el menú -----    
    
def generar_e_imprimir_reporte(tipo, rango):
    """Genera e imprime un reporte.
    
        Si el rango el reporte es inválido
        imprime un mensaje de error.
    """
    inicio, fin = rango
    reporte = realizar_reporte(tipo, inicio, fin)
    
    if 'nombres' in reporte:
        imprimir_reporte(reporte)
    else:
        utilidades.println(TEXTO_RANGO_INVALIDO)
    
    # líneas para dar formato
    utilidades.println()
    utilidades.enter_to_continue(MENSAJE_PARA_CONTINUAR)
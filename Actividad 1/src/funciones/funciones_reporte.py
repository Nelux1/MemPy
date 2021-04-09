#  mensaje que se muestra si el rango para hacer el reporte no es válido.
TEXTO_RANGO_INVALIDO = f'\N{cross mark} Por favor, especifique un rango numérico válido. FIN >= INICIO\n'


def imprimir_reporte(tipo, rango):
    """Imprime en consola los resultados del reporte.
    
        Si el rango no es válido, muestra un mensaje de error.
    """
    from . import utilidades, MENSAJE_PARA_CONTINUAR
    
    inicio, fin = rango
    
    if fin < inicio:
        utilidades.println(TEXTO_RANGO_INVALIDO)
    else:
        utilidades.println(f'Reporte sobre {tipo_str(tipo)}, en el rango ({inicio}, {fin})\n{"-" * 50}\n')
        
        reporte = realizar_reporte(tipo, inicio, fin)
        
        # imprimo en 2 columnas
        for i in range(1, len(reporte)):
            utilidades.println(f'{reporte[i - 1]["nombre"]:<15}{reporte[i]["nombre"]}')
        
        utilidades.println()
        
    utilidades.enter_to_continue(MENSAJE_PARA_CONTINUAR)


def realizar_reporte(tipo, inicio, fin):
    """Retorna lista de los alumnos que entren en el rango (inicio, fin) según tipo.
    
        Si tipo es un número, entonces se da por hecho que se desea ordenar por
        las notas de una evaluación dada.
    """
    from datos.datos import lista_alumnos
    
    if tipo == 'nota_final':
        funcion = lambda alumno: alumno[tipo] >= inicio and alumno[tipo] <= fin
    else:
        funcion = lambda alumno: alumno['notas'][tipo - 1] >= inicio and alumno['notas'][tipo - 1] <= fin
                                  
    return list(filter(funcion, lista_alumnos))


def tipo_str(tipo):
    """Retorna una versión legible del tipo de reporte."""
    if tipo == 'nota_final':
        return 'nota final'
    
    return f'evaluación {tipo}'

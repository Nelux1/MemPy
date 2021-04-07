from . import utilidades, MENSAJE_PARA_CONTINUAR

from datos.datos import lista_alumnos


def imprimir_promedio():
    """Imprime en consola los datos del promedio."""
    
    suma = 0
    
    for dicc in lista_alumnos:
        suma += dicc['nota_final']
    
    utilidades.println(f'Promedio de las notas finales: {suma / len(lista_alumnos)}')
    
    utilidades.enter_to_continue(MENSAJE_PARA_CONTINUAR)

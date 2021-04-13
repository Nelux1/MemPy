from . import utilidades, MENSAJE_PARA_CONTINUAR

from datos.datos import lista_alumnos


def ordenar_por_clave(clave):
    """Retorna lista de alumnos ordenadas por la clave dada."""
    return sorted(lista_alumnos, key= lambda dicc: dicc[clave])   


def ordenar_por_evaluacion(numero):
    """Retorna lista de alumnos ordenadas por el número de evaluación dado."""
    return sorted(lista_alumnos, key=lambda dicc: dicc['notas'][numero - 1])


def imprimir_alumno(alumno):
    """Imprime los datos de un alumno con formato."""
    print('=' * 30)
    print()
    print(f'{alumno["nombre"]}')
    print('Notas: ', end='')
    for nota in alumno['notas']:
        print(nota, end=' ')
    print() 
    print(f'Nota final: {alumno["nota_final"]}')
    print()
    print('=' * 30)


def imprimir_alumnos(lista):
    """Imprime en consola la lista de alumnos dada."""   
    for alumno in lista:
        imprimir_alumno(alumno)
    
    utilidades.enter_to_continue(MENSAJE_PARA_CONTINUAR)
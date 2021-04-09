from . import utilidades, MENSAJE_PARA_CONTINUAR

from datos.datos import lista_alumnos

# nombre, 1 o 2, notas_final
def imprimir_datos_ordenados(criterio):
    """Imprime en consola los datos ordenados."""
    lista_ordenada = ordenar(criterio)
    
    for alumno in lista_ordenada:
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
    
    utilidades.enter_to_continue(MENSAJE_PARA_CONTINUAR)
    
       
def ordenar(criterio):
    """Retorna la lista de alumnos ordenada segun el criterio dado.txt
    
        Si recibe un int, se supone que se desea ordenar en base a
        los resultados de una evaluación.
        
        Si no, puede ser por nombre o por nota final.
    """
    if isinstance(criterio, int):
        return sorted(lista_alumnos, key=lambda dicc: dicc['notas'][criterio - 1])
    else:
        return sorted(lista_alumnos, key= lambda dicc: dicc[criterio])    
    
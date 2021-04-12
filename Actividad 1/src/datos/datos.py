nom= open('../resources/nombres.txt','r', encoding='utf-8')
ev1= open('../resources/eval1.txt','r', encoding='utf-8')
ev2= open('../resources/eval2.txt','r', encoding='utf-8')


def limpiar_string(string_valores):
    """Retorna una lista a partir de los datos de un string."""
    return string_valores.replace('"', '').split(',\n')


def crear_alumno(nombre, notas):
    """Retorna un dict con los datos del alumno."""
    return {'nombre': nombre, 'notas': notas, 'nota_final': sum(notas)}


def obtener_estructura_alumnos(nombres, *notas):
    """Retorna una lista de dict de alumnos."""
    return [crear_alumno(nombres[i], [int(notas[j][i]) for j in range(len(notas))]) for i in range(len(nombres))]    


lista_alumnos = obtener_estructura_alumnos(limpiar_string(nom.read()), limpiar_string(ev1.read()), limpiar_string(ev2.read()))
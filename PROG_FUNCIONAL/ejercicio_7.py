""" Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario
    con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas. """

def calificaciones(diccionario_notas):

    diccionario_modificado = {}

    for clave, valor in diccionario_notas.items():
        if valor < 5:
            diccionario_modificado[clave.upper()] = 'SS'
        elif valor < 7:
            diccionario_modificado[clave.upper()] = 'AP'
        elif valor < 9:
            diccionario_modificado[clave.upper()] = 'NT'
        elif valor < 10:
            diccionario_modificado[clave.upper()] = 'SB'
        else:
            diccionario_modificado[clave.upper()] = 'MH'

    return diccionario_modificado




dicc = {
    'programación' : 8,
    'redes' : 7.5,
    'bases de datos' : 6.75,
    'lenguajes de marcas' : 9,
    'programación II' : 10
    }

print(calificaciones(dicc))
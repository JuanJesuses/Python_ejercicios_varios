""" Escribir una función que reciba una lista de notas y devuelva la lista de calificaciones
    correspondientes a esas notas. """

def calificaciones(notas):

    calificacion = []
    for i in range(len(notas)):
        if notas[i] > 0 and notas[i] < 5:
            calificacion.append("Suspenso")
        elif notas[i] >= 5 and notas[i] <= 7:
            calificacion.append("Aprobado")
        elif notas[i] >= 8 and notas[i] <= 9:
            calificacion.append("Notable")
        elif notas[i] == 10:
            calificacion.append("Sobresaliente")

    return calificacion


notaciones = [3,7,5,8,10,7,9,2]
print(calificaciones(notaciones))

# SOLUCIÓN DE LA WEB

def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade(scores):
    '''
    Función que devuelve la calificación correspondiente a las notas de una lista dada.
    Parámetros:
        scores: Es una lista de valores reales entre 0 y 10.
    Devuelve
        La lista de calificaciones correspondiente a las notas de scores.
    '''
    return list(map(grade, scores))

print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))
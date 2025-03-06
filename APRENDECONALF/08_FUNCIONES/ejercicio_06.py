""" Escribir una función que reciba una muestra de números en una lista y devuelva su media. """

def media(lista_num):
    # Función que calcula la media de una lista de números

    contadorNumeros = len(lista_num)
    contador = 0
    for i in lista_num:
        contador = contador + i

    return round((contador/contadorNumeros), 2)

lista = [3,5,1,98,12]

print(media(lista))

# SOLUCIÓN 1 DE LA WEB

def mean(sample):
    """Función que calcula la media de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve la media de los números en sample.
    """
    return sum(sample)/len(sample)

print(mean([1, 2, 3, 4, 5]))
print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

# SOLUCIÓN 2 DE LA WEB

def mean(*sample):
    """Función que calcula la media de una muestra de números.
    Parámetros
    *sample: Secuencia de números separados por comas.
    Devuelve la media de los números en *sample.
    """
    return sum(sample)/len(sample)

print(mean(1, 2, 3, 4, 5))
print(mean(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))
""" Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados. """

def potencia(*args):
    # Función que devuelve lista con los cuadrados de los números pasados por parámetro en una lista
    lista_cuadrados = []

    for arg in args:
        lista_cuadrados.append(pow(arg,2))

    return lista_cuadrados

print(potencia(2,4,1,3))

# SOLUCIÓN 1 DE LA WEB

def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

print(square([1, 2, 3, 4, 5]))
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

# SOLUCIÓN 2 DE LA WEB

def square(*sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    *sample: Es una secuencia de números separados por comas.
    Devuelve una lista con los cuadrados de los números de sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

print(square(1, 2, 3, 4, 5))
print(square(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))
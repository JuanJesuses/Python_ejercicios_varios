""" Escribe una función que tome un array y devuelva la media. """

def media(array):

    contador = 0

    for i in range(len(array)):
        contador += array[i]

    media = contador / len(array)

    return media

array_numeros = [12,73,41,18,54,702]
print('La media es: ',media(array_numeros))
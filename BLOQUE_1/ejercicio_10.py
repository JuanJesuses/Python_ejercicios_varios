""" Escribe una función que tome un array e imprima cada elemento individualmente. """

def imprimeArray(array):

    for i in range(len(array)):
        print("El elemento",i,"es: ", array[i])


arreglo = [21,'hoy', 15.6,[34,22,'espacio'],'array',27,{1:2,3:4,5:6}]

imprimeArray(arreglo)
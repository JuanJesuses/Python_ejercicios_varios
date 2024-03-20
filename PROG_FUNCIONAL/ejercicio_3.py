""" Ejemplo:

    def cuadrado(x):
        return x ** 2

    def raiz_cuadrada(x):
        return x ** 0.5

    def operar(func, *args):
        for n in args:
            print(func(n))
    print(operar(cuadrado, 2,3,5)) """

""" Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar
    la función dada a cada uno de los elementos de la lista. """

def suma(listaSuma):

    totalSuma = 0
    for i in range(len(listaSuma)):
        totalSuma = totalSuma + listaSuma[i]

    return totalSuma

def refuncion(lista, *args):

    for n in args:
        print(lista(n))


refuncion(suma,[1,2,3,4,5,6,7,8,9])

# Esto es una prueba
# de un comentario
# multilínea
# dando al intro

""" Esto es una prueba de un comentario
    multilínea dando al intro sin almohadillas. """
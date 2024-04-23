""" Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas,
    y muestre por pantalla cada uno de los productos en una línea distinta. """

cesta = input('Introduce la cesta de la compra separando los productos por comas: ')
compra = cesta.split()

for i in compra:
    print(i[:i.find(',')])


# SOLUCIÓN DE LA WEB 1

cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print(cesta.replace(',', '\n'))

# SOLUCIÓN DE LA WEB 2

cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print('\n'.join(cesta.split(',')))
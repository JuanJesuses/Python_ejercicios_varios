""" Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el
    artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar
    por pantalla la lista de la compra y el coste total, con el siguiente formato

    Lista de la compra

    Artículo 1	Precio
    Artículo 2	Precio
    Artículo 3	Precio
    …	…
    Total	    Coste """

cesta_compra = {}
continuar = True
total = 0
coste = ('Total')

while continuar:
    articulo = input("Introduzca el nombre del artículo: ")
    cesta_compra[articulo] = float(input("Introduzca el precio del artículo: "))
    continuar = input("¿Quiere introducir otro artículo? (s/n): ") == 's'
    total += cesta_compra.get(articulo)

for articulo, precio in cesta_compra.items():
    print("{:<10}{:>20.2f}".format(articulo, precio))

print("{:<10}{:>20.2f}".format(coste,total))

# SOLUCIÓN DE LA WEB

cesta = {}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = precio
    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
coste = 0
print('Lista de la compra')
for item, precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)
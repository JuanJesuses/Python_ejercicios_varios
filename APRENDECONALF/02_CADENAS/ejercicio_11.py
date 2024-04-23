""" Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por
    pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
    el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales. """

# Pedir al usuario:

#   1. nombre del producto
#   2. precio
#   3. Número de unidades

# Mostrar por pantalla:

#   1. cadena con el nombre del producto
#   2. precio unitario con 6 dígitos enteros y dos decimales
#   3. número de unidades con tres dígitos
#   4. coste total con 8 dígitos enteros y dos decimales

# ============== * ==============

# SOLUCIÓN DE LA WEB. NO HE SABIDO INTERPRETAR

producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print(
    '{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto=producto, unidades=unidades,
                                                                                  precio=precio,
                                                                                  total=unidades * precio))

""" Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares
    desde 1 hasta ese número separados por comas. """

num = int(input("Introduce un número: "))

for i in range(1, (num + 1)):
    if i % 2 != 0 and i == (num - 1):
        print(f"{i}")
    elif i % 2 != 0 and i != num:
        print(f"{i},", end="")

# SOLUCIÓN DE LA WEB

n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")
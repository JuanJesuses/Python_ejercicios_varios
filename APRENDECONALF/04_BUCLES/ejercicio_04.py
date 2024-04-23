""" Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese
    número hasta cero separados por comas. """

num = int(input("Introduzca un número positivo: "))

for i in range(num + 1):
    if num - i == 0:
        print(f"{num - i}")
    else:
        print(f"{num - i},", end="")

# SOLUCIÓN DE LA WEB

n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")
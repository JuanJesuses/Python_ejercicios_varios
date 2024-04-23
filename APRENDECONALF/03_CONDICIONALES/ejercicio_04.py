""" Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar. """

num = int(input("Introduzca un número: "))

if num % 2 == 0:
    print(f'El número {num} es par.')
else:
    print(f'El número {num} es impar.')
""" Finger exercise: Write a program that asks the user to input 10 integers, and then prints the largest odd number
    that was entered. If no odd number was entered, it should print a message to that effect."""

contador = 10
swap = 0

while contador > 0:
    entero = int(input("Introduce un entero: "))
    if entero > swap and entero % 2 != 0:
        swap = entero
    contador -= 1

if swap:
    print("El mayor de los impares es", swap)
else:
    print("no se han introducido números impares.")
""" Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en
    líneas distintas el nombre del usuario tantas veces como el número introducido. """

nombre = input("What's your name?: ")
num = int(input('How long times?: '))

for i in range(num):
    print(nombre)

# Solución de la web
print((nombre + "\n") * int(num))
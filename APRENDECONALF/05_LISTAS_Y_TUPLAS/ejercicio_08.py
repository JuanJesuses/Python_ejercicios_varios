""" Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo. """

palabra = input("Introduzca una palabra: ")
mitad = int((len(palabra)) / 2)
reverso = ""

for i in range(len(palabra),mitad,-1):
    print(palabra[i-1], end="")
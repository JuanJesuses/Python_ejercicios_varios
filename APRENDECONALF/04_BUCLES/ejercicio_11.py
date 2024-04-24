""" Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la
    palabra introducida empezando por la última. """

palabra = input("Introduce una palabra: ")

for i in range(1,len(palabra) + 1):
    print(palabra[-i], end=" ")

# SOLUCIÓN DE LA WEB

word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])
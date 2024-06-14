""" Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo. """

palabra = input("Introduzca una palabra: ")
mitad = int((len(palabra)) / 2)
reverso = -1


for i in range(mitad):
    if palabra[i] == palabra[reverso]:
        reverso -= 1
    else:
        print("No es un palíndromo.")
        exit()

print("Es un palíndormo.")

# VERSIÓN 2

palabra = input("Introduzca una palabra: ")
mitad = int((len(palabra)) / 2)
contador = 0
reverso = -1


for i in range(mitad):
    if palabra[i] == palabra[reverso]:
        contador += 1
        reverso -= 1
    else:
        print("No es un palíndromo.")
        exit()

if contador == mitad:
    print("Es un palíndormo.")


# SOLUCIÓN DE LA WEB

word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
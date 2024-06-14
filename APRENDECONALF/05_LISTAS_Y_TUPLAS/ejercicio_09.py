""" Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene
    cada vocal. """

palabra = input("Introduzca una palabra: ")
vocales = 'aeiou'
suma_vocales = []
contador = 0

for i in range(len(palabra)):
    if palabra[i] in vocales:
        suma_vocales.append(palabra[i])

for i in range(len(vocales)):
    for j in range(len((suma_vocales))):
        if vocales[i] in suma_vocales[j]:
            contador += 1

    print(f"Hay {contador} {vocales[i]}.")
    contador = 0

# SOLUCIÓN DE LA WEB

word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals:
    times = 0
    for letter in word:
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")
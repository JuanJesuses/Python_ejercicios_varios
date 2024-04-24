""" Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número
    de veces que aparece la letra en la frase. """

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
contador = 0

for i in frase:
    if letra == i:
        contador += 1

print(f"La letra {letra} aparece {contador} veces en la frase '{frase}'")

# SOLUCIÓN DE LA WEB

frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
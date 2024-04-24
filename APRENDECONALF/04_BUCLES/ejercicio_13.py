""" Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba 'salir'
    que terminará. """

palabras = ""

while 'salir' not in palabras:
    palabras = input("Escriba lo que sea: ")
    print(palabras)

# SOLUCIÓN DE LA WEB

while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)
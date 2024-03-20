""" Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud. """

def dicc_frase(frase):

    palabras = frase.split()
    diccioPalabras = {}

    for i in palabras:
        diccioPalabras[i] = len(i)

    return diccioPalabras


print(dicc_frase("Esto es una frase."))

# SOLUCIÓN DE LA WEB

def length_words(sentence):

    words = sentence.split()
    lenghts = map(len,words)
    return dict(zip(words, lenghts))

print(length_words('Welcome to Python'))

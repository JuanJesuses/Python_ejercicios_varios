""" Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!. """

def saludo(nombre):
    "Función que muestra un saludo al nombre pasado por parámetro"
    print(f"Hola, {nombre}")
    return

nombre = input("Introduzca el nombre para saludar: ")

saludo(nombre)
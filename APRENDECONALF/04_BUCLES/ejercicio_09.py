""" Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la
    contraseña hasta que introduzca la contraseña correcta. """

palabra = "contraseña".lower()

clave = input("Introduzca la clave: ")

while clave.lower() != palabra.lower():
    clave = input("Contraseña incorrecta, inténtelo de nuevo: ")

print("ACCESO CONCEDIDO!!")

# SOLUCIÓN DE LA WEB

key = "contraseña"
password =""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")
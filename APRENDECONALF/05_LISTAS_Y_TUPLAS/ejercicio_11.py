""" Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su
    producto escalar. """

# Como no tengo ni idea de lo que pide el ejercicio, pongo directamente la solición de la web

# SOLUCIÓN DE LA WEB

a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) 
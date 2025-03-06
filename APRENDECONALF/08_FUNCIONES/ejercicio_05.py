""" Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la
    primera función. """
import math
def areaCirculo(radio):
    # Función que calcula el área del círculo

    rCuadrado = radio**2

    return round((3.1415 * rCuadrado), 2)

def volumenCilindro(r, h):
    # Función que calcula el volumen de un cilindro

    # rCuadrado = areaCirculo(r)*h

    return round((areaCirculo(r) * h), 2)


radio = float(input("Introduce el radio: "))

print(f"El area del círculo es: {areaCirculo(radio)}")

opcion = input("¿Quiere calcular el área del cilindro? (s/n)")

if opcion == 's':
    altura = float(input("Introduce la altura: "))
    print(f"El volumen del cilindro es: {volumenCilindro(radio, altura)}")
else:
    pass

# SOLUCIÓN DE LA WEB

def circle_area(radius):
    """Función que calcula el area de un círculo.
       Parámetros
       radius: Es el radio del círculo.
       Devuelve el área del círculo de radio radius."""
    pi = 3.1415
    return pi*radius**2

def cilinder_volume(radius, high):
    """Función que calcula el volumen de un cilindro.
    Parámetros
    radius: Es el radio de la base del cilindro.
    high: Es la altura del cilindro.
    Devuelve el volumen del clindro de radio radius y altura high.
    """
    return circle_area(radius)*high

print(cilinder_volume(3,5))

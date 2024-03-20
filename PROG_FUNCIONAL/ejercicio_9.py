""" Escribir una función que calcule el módulo de un vector.
    v = sqrt(v1**2 + v2**2) """
import math

def calculoModuloVector(v1, v2):

    cuadrados = pow(v1,2) + pow(v2, 2)
    v =  math.sqrt(cuadrados)

    return v

print(calculoModuloVector(-3,-4))
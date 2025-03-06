""" Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común
    múltiplo. """

from math import gcd

def mcd(num1, num2):
    # Función que calcula el Máximo Comun Divisor de dos números
    maxcd = gcd(num1,num2)
    return maxcd

def mcm(num1, num2):
    # Función que calcula el Mínimo Común Múltiplo de dos números
    mincd = ((int(num1*num2))/mcd(num1,num2))
    return mincd

x = 300
y = 33880
maximo = mcd(x,y)
minimo = mcm(x,y)

print(f'El MCD de {x} y {y} es: {maximo}')
print("El Mínimo Común Múltiplo de {} y {} es {}".format(x,y,minimo))

# SOLUCIÓN DE LA WEB

def mcd(n, m):
    """Función que calcula el máximo común divisor de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))
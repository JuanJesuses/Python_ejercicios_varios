""" Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y
    muestre por pantalla su media y desviación típica. """
import math
from math import sqrt

lista_num = []
num = 1


def media(lista_num):
    media = 0
    suma = 0

    for i in range(len(lista_num)):
        suma += lista_num[i]

    media = suma / len(lista_num)

    return media

def varianza(media_nums, lista_num):

    calc1 = 0

    for i in range(1,len(lista_num)+1):
        calc1 += (pow(i,2))

    calc2 = round((calc1 / len(lista_num)) - pow(media_nums, 2), 2)

    print(calc1)

    return calc2

while num != 0:
    num = int(input("Introduce un número: "))
    if num != 0:
        lista_num.append(num)

desv_tipica = round(sqrt(varianza(media(lista_num), lista_num)),2)

# print(media(lista_num), varianza(media(lista_num), lista_num))
print(media(lista_num), desv_tipica)

# RESULTADO DE LA WEB. NO HE CONSEGUIDO IDENTIFICAR EL ERROR: VALUE ERROR: MATH DOMAIN ERROR

sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)
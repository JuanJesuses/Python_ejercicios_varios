""" Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media,
    varianza y desviación típica. """
import math

""" 
 FÓRMULA DESVIACIÓN TÍPICA:
 
 1. Calcular la media
    x = (2 + 4 + 4 +6 + 8 / 5) = 24/5 = 4.8

 2. Hallar las diferencias al cuadrado respecto de la media
    (2 - 4.8)**2 = (-2.8)**2 = 7.84
    (4 - 4.8)**2 = (-0.8)**2 = 0.64
    (4 - 4.8)**2 = (-0.8)**2 = 0.64
    (6 - 4.8)**2 = (1.2)**2 = 1.44
    (8 - 4.8)**2 = (3.2)**2 = 10.24
 
3. Suma las desviaciones al cuadrado
    7.84 + 0.64 + 0.64 + 1.44 + 10.24 = 20.8

4. Sustituir los valores en la fórmula
    s = sqrt((20.8)/5-1)
    s = sqrt(5.2)
    s +/- = 2.28
 
 """

def media(lista_num):
    # Función que calcula la media de una lista de números

    contadorNumeros = len(lista_num)
    contador = 0
    for i in lista_num:
        contador = contador + i

    return round((contador/contadorNumeros),2)

#print(media(1,2,3))

def varianza(lista):
    # Función que calcula la varizanza de una lista de números
    mean = media(lista)

    lista_sum = []
    for i in lista:
        lista_sum.append(pow((i - mean),2))

    #print(lista_sum)

    return round(sum(lista_sum)/len(lista_sum),2)

def desviacion_tipica(lista):
    # Función que calcula la desviación típica

    # Calculamos la media llamando a la función media pasándole como parámetro la lista dada
    calculo_media = media(lista)

    # Creamos una lista vacía para introducir las diferencias al cuadrado respecto de la media
    lista_diferencia = []
    for i in lista:
        lista_diferencia.append(round(pow((i-calculo_media),2),2))

    # Creamos una variable para almacenar la suma de las diferencias al cuadrado respectp de la media
    suma_diferencias = 0
    for j in lista_diferencia:
        suma_diferencias += j

    sus_valores = suma_diferencias / (calculo_media - 1)

    desv_tipica = math.sqrt(sus_valores)

    #print(calculo_media,"\n",lista_diferencia,"\n",round(suma_diferencias,2),"\n",round(desv_tipica,2))

    return round(desv_tipica)


medavadesv = {}
lista = [0,2,4,5,8,10,10,15,38]
#print(varianza(lista), media(lista))
desviacion_tipica(lista)

for z in lista:
    medavadesv[z] = (media(lista),varianza(lista), desviacion_tipica(lista))

print(medavadesv)

# SOLUCIÓN DE LA WEB

def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(sample):
    """Función que calcula la media, varianza y desviación típica de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    """
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

#print(statistics([1, 2, 3, 4, 5]))
#print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
print(statistics([0,2,4,5,8,10,10,15,38]))
print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

# SOLUCIÓN 2 DE LA WEB

def square(*sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una secuencia de números separados por comas.
    Devuelve una lista con los cuadrados de los números de sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(*sample):
    """Función que calcula la media, varianza y desviación típica de una muestra de números.
    Parámetros
    sample: Es una secuencia de números separados por comas.
    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    """
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(*sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics(1, 2, 3, 4, 5))
print(statistics(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))
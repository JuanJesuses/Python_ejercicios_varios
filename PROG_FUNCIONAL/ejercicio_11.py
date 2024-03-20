""" Ejercicio 11
    Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir,
    los valores cuya puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación típica de un valor
    se obtiene restando la media y dividiendo por la desviación típica de la muestra. """
import math

def calcula_media(lista_valores):
    totales = 0
    longitud = len(lista_valores)
    for i in range(len(lista_valores)):
        totales = totales + lista_valores[i]

    media = totales / longitud

    return media

def calcula_mediana(lista_valores):
    lista_valores.sort()

    if len(lista_valores) % 2 != 0:
        mediana1 = int((len(lista_valores) / 2) + 0.5)
        mediana = lista_valores[mediana1 - 1]
    else:
        mediana1 = int((len(lista_valores) / 2))
        mediana = (lista_valores[int(mediana1)] + lista_valores[int(mediana1) - 1]) / 2

    return mediana

def calcula_desviacion_tipica(lista_valores, media):

    suma_lista_desv_tipica = 0

    for x in range(len(lista_valores)):
        suma_lista_desv_tipica = suma_lista_desv_tipica + (pow((lista_valores[x] - media),2))

    desviacion_tipica = round(math.sqrt((suma_lista_desv_tipica)/media),2)

    return desviacion_tipica

def valores_atipicos(lista_valores, media, desviacion_tipica):

    atipica = []
    tipica = []
    diccionario_atipico = {}
    diccionario_tipico = {}

    for i in range(len(lista_valores)):
        puntuacion_tipica = round(((lista_valores[i] - media) / desviacion_tipica),2)
        if puntuacion_tipica > 3 or puntuacion_tipica < -3:
            atipica.append(puntuacion_tipica)
            diccionario_atipico[lista_valores[i]] = puntuacion_tipica
        else:
            tipica.append(puntuacion_tipica)
            diccionario_tipico[lista_valores[i]] = puntuacion_tipica

    return diccionario_atipico
    #return atipica

lista_valores = [108, 31, 75, 87, 79, 88, 89, 118, 51, 89, 174, 95, 51, 70 , 73]
media = calcula_media(lista_valores)
mediana = calcula_mediana(lista_valores)
desviacion_tipica = calcula_desviacion_tipica(lista_valores, media)

print(valores_atipicos(lista_valores, media, desviacion_tipica))
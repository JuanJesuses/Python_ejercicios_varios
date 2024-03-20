""" Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

    [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
     {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
     {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
     {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
     {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

    Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. La función recibirá
    como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o
    igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con
    el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

    Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
    Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5 """

def buscaImnuebles(viviendas, precio_busqueda):

    viviendas_guardadas = []

    for i in (viviendas):
        if i.get('zona') == 'A':
            precio = ((i.get('metros') * 1000 + i.get('habitaciones') * 5000
                       + i.get('garaje') * 15000) * (i.get('año') / 100 - 1))
            if precio <= precio_busqueda:
                viviendas_guardadas.append(i)
        elif i.get('zona') == 'B':
            precio = (((i.get('metros') * 1000 + i.get('habitaciones') * 5000
                        + i.get('garaje') * 15000) * (i.get('año') / 100 - 1)) * 1.5)
            if precio <= precio_busqueda:
                viviendas_guardadas.append(i)

    return viviendas_guardadas

bbdd_viviendas = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
                  {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
                  {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
                  {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
                  {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

print(buscaImnuebles(bbdd_viviendas, 2000000))
print(len(buscaImnuebles(bbdd_viviendas, 2000000)))

"""  
    PRECIO A: precio = ((viviendas[i].get('metros') * 1000 + viviendas[i].get('habitaciones') * 5000
                       + viviendas[i].get('garaje') * 15000) * (1 - viviendas[i].get('año')/100))

    PRECIO B: precio = (((viviendas[i].get('metros') * 1000 + viviendas[i].get('habitaciones') * 5000
                        + viviendas[i].get('garaje') * 15000) * (1 - viviendas[i].get('año')/100)) * 1.5)
"""
""" Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un
    programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el
    precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total. """

pan = 3.49
discount = (pan * 60) / 100
pan_podrio = pan - discount

barras_vendidas = int(input("Introduzca el número de barras podrías vendidas: "))
precio_total = round(barras_vendidas * pan_podrio)

print(f'El precio de una barra de pan es de {pan} euros, el descuento por no ser fresca es de {discount} euros\n'
      f'El total de las barras adquiridas es de {precio_total} euros')
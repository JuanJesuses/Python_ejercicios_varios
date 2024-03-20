""" Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
    y muestre por pantalla el capital obtenido en la inversión. """

cantidad_invertida = float(input("Indique la cantidad a invertir: "))
interes_anual = float(input("Indique el interés anual: "))
annos = int(input("Indique el número de años: "))

interes_anual = (interes_anual / 100 + 1) ** annos

cantidad_total = round((cantidad_invertida * interes_anual),2)
print(cantidad_total)
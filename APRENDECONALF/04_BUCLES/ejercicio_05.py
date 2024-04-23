""" Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y
    muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
    Fórmula - (capital * tasa * tiempo)"""

cantidad = float(input("Introduzca la cantidad a invertir: "))
interes = float(input("Introduzca el interés: "))
annos = int(input("Introduzca los años: "))
ganancia = 0

for i in range(1, annos + 1):
    calculo = (cantidad * interes)/100
    cantidad = cantidad + calculo
    print(f"Ganancias año {i}: {cantidad}")

# SOLUCIÓN DE LA WEB

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))
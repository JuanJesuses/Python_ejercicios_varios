""" Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a
    1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por
    pantalla si el usuario tiene que tributar o no. """

edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos: "))

if edad > 16 and ingresos >= 1000.00:
    print("Hermano, tienes que tributar.")
elif edad <= 16 and ingresos < 1000.00:
    print("Hermano, no tienes ni la edad ni los ingresos para tributar.")
elif edad <= 16 and ingresos >= 1000.00:
    print("Hermano, ganas la pasta pero no tienes la edad.")
elif edad > 16 and ingresos < 1000.00:
    print("Hermano, tienes la edad pero eres un puto pobre.")
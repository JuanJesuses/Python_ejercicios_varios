""" Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
    Después debe mostrar por pantalla la paga que le corresponde. """

horas_trabajadas = int(input('¿Cuántas horas has trabajado?: '))
coste_hora = 7.50
paga = horas_trabajadas * coste_hora

print(f'Te corresponden: {paga} Euros.')
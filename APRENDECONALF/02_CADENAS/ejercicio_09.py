""" Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
    el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se
    introduzcan con un solo carácter. """

f_nac = input("Introduzca su fecha de nacimiento en formato dd/mm/aaaa: ")

dia = f_nac[:f_nac.find('/')]
mes = f_nac[f_nac.find('/') + 1:f_nac.rfind('/')]
anno = f_nac[f_nac.rfind('/') + 1:]

print(f'Día: {dia}')
print(f'Mes: {mes}')
print(f'Año: {anno}')


# SOLUCIONES DE LA WEB

""" Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
    el día, el mes y el año. """

fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])

# Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)

# Esto es un error mío de interpretación del ejercicio
# Validar cantidad de caracteres en la inserción de fecha
"""
if f_nac[2] != '/' and f_nac[4] != '/':
    f_nac = '0' + f_nac
    f_nac = f_nac[:2] + '/0' + f_nac[3:]
elif f_nac[2] != '/':
    f_nac = '0' + f_nac
elif f_nac[5] != '/':
    f_nac = f_nac[:3] + '0' + f_nac[3:]

print(f_nac) """
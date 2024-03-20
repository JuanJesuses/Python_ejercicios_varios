""" Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en
    formato dd de <mes> de aaaa donde <mes> es el nombre del mes. """

meses = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
    7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
    }

fecha = input("Introduce una fecha con el formato (dd/mm/aaaa): ")

dia = fecha[0:2]
mes_num = int(fecha[3:5])
mes = meses.get(mes_num)
anio = fecha[-4:]

print(f'{dia} de {mes} de {anio}')

# --------- SOLUCIÓN DE LA WEB --------- #

meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])
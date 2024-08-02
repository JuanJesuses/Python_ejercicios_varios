""" Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato
    dd de <mes> de aaaa donde <mes> es el nombre del mes. """

meses = {'01':'enero', '02':'febrero', '03':'marzo', '04':'abril', '05':'mayo', '06':'junio',
         '07':'julio', '08':'agosto', '09':'septiembre', '10':'octubre', '11':'noviembre', '12':'diciembre'}

fecha = input("Introduzca una fecha (formato dd/mm/aaaa): ")

print(f"{fecha[0:2]} de {meses.get(fecha[3:5])} de {fecha[6:10]}")

# SOLUCIÓN DE LA WEB

meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])
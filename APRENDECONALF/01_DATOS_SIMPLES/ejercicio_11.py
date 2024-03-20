""" Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido
    a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir
    un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el
    usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y
    tercer años. Redondear cada cantidad a dos decimales. """

amount = float(input("Introduzca la cantidad de dinero depositada en la cuenta de ahorros: "))
interes_anual = 4

anno1 = round(((amount * 4) / 100),2)

print(f'La cantidad de ahorros del primer año es: {anno1+amount}\n'
      f'Segundo año: {(anno1*2) + amount}\n'
      f'Tercer año: {(anno1*3) + amount}')
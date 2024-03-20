""" Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
    Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular
    el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
    Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total
    del paquete que será enviado. """

payasos = 112.0
munecas = 75.0

pedido_payasos = int(input("¿Cuántos payasos se han enviado en el último pedido?: "))
pedido_munecas = int(input("¿Cuántas muñecas se han enviado en el último pedido?: "))

peso_total = ((pedido_payasos * payasos) + (pedido_munecas * munecas))/100

print(f'El peso total del último pedido es de {peso_total} gramos.')
""" Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en
    un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
    El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea
    añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea
    pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación
    el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro. """

facturas = {}
cobrado = []

def mostrar_facturas():

    pago = 0
    for num_fra, importe in facturas.items():
        pago += importe

    return round(pago,2)

def pagar_fra():

    cobros = 0
    numero_fra = input("Introduzca el número de factura a pagar: ")
    cobros += facturas[numero_fra]
    cobrado.append(cobros)

    del facturas[numero_fra]

def gestionar_pago_fra():

    cobro = 0
    for i in cobrado:
        cobro += i

    return round(cobro,2)

def agregar_fra():
    pte_cobro = 0
    num_fra = input("Introduca el número de factura: ")
    facturas[num_fra] = float(input("Introduzca el importe de la factura: "))
    pte_cobro += facturas[num_fra]

def mostrar_facturas_importes():

    for pago, cobro in facturas.items():
        print(f"Número de factura: {pago}, - Importe factura: {cobro}")


# MENÚ FACTURAS
continuar = 1

while continuar > 0 and continuar < 4:
    print("1. Añadir factura \n2. Pagar Factura \n3. Mostrar Facturas \n4. Terminar")
    accion = int(input("¿Qué operación desea realizar?: "))
    if accion == 1:
        agregar_fra()
        print(f"El importe de las facturas pendientes es de {mostrar_facturas()} euros.")
        print(f"El importe de las facturas cobradas es de {gestionar_pago_fra()} euros.")
    elif accion == 2:
        pagar_fra()
        print(f"El importe de las facturas pendientes es de {mostrar_facturas()} euros.")
        print(f"El importe de las facturas cobradas es de {gestionar_pago_fra()} euros.")
    elif accion == 3:
        print(mostrar_facturas_importes())
    elif accion == 4:
        print("Operación finalizada.")
        continuar = 4

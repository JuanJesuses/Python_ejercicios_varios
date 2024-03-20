""" Ejercicio 1

    Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una
    tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las
    funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta
    y devolver el precio final de la cesta. """

def calcular():

    mostrarMenu()
    opcion = int(input("Escoge una opción del menú: "))

    while opcion > 0 and opcion < 4:

        if opcion == 1:
            cestaAMostrar = int(input("Escoge una de las cuatro cestas (1-4): "))
            diccionario = mostrarCestas(cestaAMostrar)
            calculaPrecios(diccionario,1)
        elif opcion == 2:
            cestaAMostrar = int(input("Escoge una de las cuatro cestas (1-4): "))
            diccionario = mostrarCestas(cestaAMostrar)
            calculaPrecios(diccionario,2)
        elif opcion == 3:
            cestaAMostrar = int(input("Escoge una de las cuatro cestas (1-4): "))
            diccionario = mostrarCestas(cestaAMostrar)
            calculaPrecios(diccionario, 3)

        pregunta = input("¿Otro cálculo?: ")
        print()

        if pregunta == 's':
            mostrarMenu()
            opcion = int(input("Escoge una opción del menú: "))
        else:
            opcion = 4

def mostrarCestas(numcesta):

    cestaDeLaCompra1 = {
        "pescado": [4.5, 7, 'normal'],
        "carne": [6.78, 4, 'normal'],
        "patatas": [1.5, 0.25, 'reducido'],
        "agua": [0.78, 0.12, 'superreducido']
    }

    cestaDeLaCompra2 = {
        "huevos": [2.25, 5, 'normal'],
        "aceite": [18.60, 12, 'reducido'],
        "fruta": [4.8, 1.15, 'reducido'],
        "congelados": [7.56, 2.10, 'normal'],
        "menaje": [15.70, 15, 'normal']
    }

    cestaDeLaCompra3 = {
        "pan": [0.6, 0.01, 'superreducido'],
        "carne": [5.70, 4, 'normal'],
        "leche": [6.3, 1.43, 'normal'],
        "agua": [5.8, 0.15, 'reducido']
    }

    cestaDeLaCompra4 = {
        "pasta": [2.35, 2, 'normal'],
        "legumbres": [3.18, 1.13, 'normal'],
        "verdura": [7.3, 1.04, 'reducido'],
        "refrescos": [12.26, 0.25, 'normal'],
        "aperitivos": [10.80, 0.06, "normal"],
        "ropa": [25.40, 2.63, "normal"]
    }

    if numcesta == 1:
        print("Esta es la cesta de la compra número 1: ")
        for clave, valor in cestaDeLaCompra1.items():
            print(clave, valor)
        return cestaDeLaCompra1
    elif numcesta == 2:
        print("Esta es la cesta de la compra número 2: ")
        for clave, valor in cestaDeLaCompra2.items():
            print(clave, valor)
        return cestaDeLaCompra2
    elif numcesta == 3:
        print("Esta es la cesta de la compra número 3: ")
        for clave, valor in cestaDeLaCompra3.items():
            print(clave, valor)
        return cestaDeLaCompra3
    elif numcesta == 4:
        print("Esta es la cesta de la compra número 4: ")
        for clave, valor in cestaDeLaCompra4.items():
            print(clave, valor)
        return cestaDeLaCompra4


def mostrarMenu():

    print("###--- CALCULADORA DE IVA Y DESCUENTOS ---###")
    print("1. CALCULAR EL IVA")
    print("2. CALCULAR LOS DESCUENTOS")
    print("3. CALCULAR IVA Y DESCUENTOS")
    print("4. SALIR")
    print()

def mostrarResultados(resultadoCalculo):

    print("El resultado es: ", resultadoCalculo)

def calculaDescuento(precio, descuento):

    descuento = descuento / 100
    cantidadADescontar = precio * descuento

    return cantidadADescontar

def calculaIva(cantidad, tipoIva):

    precioConIva = 0

    if tipoIva == 'normal':
        precioConIva = round((cantidad * 0.21),2)
    elif tipoIva == 'reducido':
        precioConIva = round((cantidad * 0.10),2)
    elif tipoIva == 'superreducido':
        precioConIva = round((cantidad * 0.04),2)

    return precioConIva

def calculaPrecios(dicc, opcion):

    precioListaDeLaCompra = 0
    valorIva = 0
    valorDescuento = 0

    if opcion == 1:
        for clave, valor in dicc.items():
            valorIva = calculaIva(valor[0], valor[2])
            precioListaDeLaCompra = precioListaDeLaCompra + valorIva

        mostrarResultados("El precio del IVA es: ", round(precioListaDeLaCompra, 2))

    elif opcion == 2:
        for clave, valor in dicc.items():
            valorDescuento = calculaDescuento(valor[0], valor[1])
            precioListaDeLaCompra = precioListaDeLaCompra + valorDescuento

        mostrarResultados("El descuento es: ", round(precioListaDeLaCompra, 2))

    elif opcion == 3:
        for clave, valor in dicc.items():
            valorIva = calculaIva(valor[0],valor[2])
            valorDescuento = calculaDescuento(valorIva, valor[1])
            precioListaDeLaCompra = precioListaDeLaCompra + (valor[0] + valorDescuento)

        mostrarResultados("El precio total es: ", round(precioListaDeLaCompra, 2))

def mostrarResultados(tipoRes, eleccionUsuario):

    print(tipoRes, eleccionUsuario)

calcular()
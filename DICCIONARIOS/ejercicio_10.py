""" Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán
    en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos
    del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de
    un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú:
    (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
    (5) Listar clientes preferentes, (6) Terminar.
    En función de la opción elegida el programa tendrá que hacer lo siguiente:

    Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    Preguntar por el NIF del cliente y mostrar sus datos.
    Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    Terminar el programa. """

cliente = {} # Diccionario que almacena los clientes

def mostrarMenu():

    print("1. Añadir cliente.")
    print("2. Eliminar cliente.")
    print("3. Mostrar cliente.")
    print("4. Listar todos los clientes.")
    print("5. Listar clientes preferentes.")
    print("6. Terminar.")

    menu()

def escogerMenu(respuesta):

    menu(respuesta)

def menu():

    opcion = int(input("Escoge una opción: "))

    if opcion == 1:
        addClient()
    elif opcion == 2:
        delClient()
    elif opcion == 3:
        mostrarRegistro()
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        print("El programa ha finalizado")


# BLOQUE DE FUNCIONES

def addClient():
    continuar = True
    datos = {}

    while continuar:
        nifCli = input("Introudce el NIF del cliente: ")
        nombreCli = input("Introduce el nombre del cliente: ")
        datos["Nombre"] = nombreCli
        addrCli = input("Introduce la dirección del cliente: ")
        datos["Direccion"] = addrCli
        telCli = input("Introduce el teléfono del cliente: ")
        datos["Teléfono"] = telCli
        emailCli = input("Introduce el email del cliente: ")
        datos["email"] = emailCli
        preferente = input("¿Es cliente preferente? (s / n):")
        prefCli = None
        if preferente == 's':
            prefCli = True
            datos["Preferente"] = True
        else:
            prefCli = False
            datos["Preferente"] = False

        cliente[nifCli] = datos

        continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

    mostrarMenu()

def delClient():

    usuario = input("Introduzca el NIF del usuario que desea eliminar: ")
    cliente.pop(usuario,"El usuario no existe.")

    mostrarMenu()


def mostrarRegistro():

    usuario = input("Introduzca el NIF del usuario: ")
    print(cliente[usuario])

    mostrarMenu()

mostrarMenu()

#print("Fin.")
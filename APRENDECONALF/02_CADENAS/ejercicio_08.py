""" Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por
    pantalla el número de euros y el número de céntimos del precio introducido. """

precio = input("Introduzca el precio: ")
print("El precio es de " + precio[:precio.find('.')] + " euros y " + precio[precio.find('.') + 1:] + " céntimos.")

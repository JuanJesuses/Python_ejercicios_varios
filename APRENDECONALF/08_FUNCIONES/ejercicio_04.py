""" Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad
    sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el
    porcentaje de IVA, deberá aplicar un 21%. """

def calculaIva(bruto, iva=21):
    """ Función que calcula el IVA de una factura. Si no se le pasa el IVA, lo calcula sobre el 21% """

    calculoIva = iva/100
    totalIva = bruto * calculoIva
    totalFactura = bruto + totalIva

    return round(totalFactura,2)


cantSin = float(input("Introduzca la cantidad bruta: "))
iva = int(input("Introduzca el IVA a aplicar: "))

print(f"Total Factura: {calculaIva(cantSin,iva)}")

# SOLUCIÓN DE LA WEB

def invoice(amount, vat=21):
    """Función de aplica el IVA a una factura.
    Parametros
    amount: Es la cantidad sin IVA
    vat: Es el porcentaje de IVA
    Devuelve el total de la factura una vez aplicado el IVA.
    """
    return amount + amount*vat/100

print(invoice(2563.12,14))
print(invoice(2563.12))
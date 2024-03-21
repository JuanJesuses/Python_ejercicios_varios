""" Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro
    correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es. """

correo = input("Introduce una dirección de correo electrónico: ")
arroba = correo.find('@')
dominio = 'ceu.es'
correo = (correo[:arroba+1]) + dominio

print(f'La nueva dirección de correo es: {correo}')

# Solución de la web

email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es')
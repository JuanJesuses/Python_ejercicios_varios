""" La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada
    tipo de pizza aparecen a continuación.

    Ingredientes vegetarianos: Pimiento y tofu.
    Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

    Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le
    muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la
    mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
    vegetariana o no y todos los ingredientes que lleva. """

def mostrar_menu(tipo_pizza):

    if tipo_pizza == "v":
        print("MENÚ VEGETARIANO:\n"
              "1. Pimiento Rojo\n"
              "2. Tofu")
    else:
        print("MENU NO VEGETARIANO:\n"
              "1. Pepperoni\n"
              "2. Jamón\n"
              "3. Salmón")

pregunta_pizza = input("¿Pizza vegetariana o de carne? (v/c): ")
mostrar_menu(pregunta_pizza)
ingrediente = int(input("\nEscoja un ingrediente: "))

pizza_v = ['Pimiento Rojo', 'Tofu']
pizza_c = ['Pepperoni', 'Jamón', 'Salmón']

if pregunta_pizza == 'v':
    print("\nHa escogido una pizza vegetariana con los siguientes ingredientes: \n"
          f"Tomate, Mozzarella, {pizza_v[ingrediente - 1]}")
else:
    print("\nHa escogido una pizza no vegetariana con los siguientes ingredientes: \n"
          f"Tomate, Mozzarella, {pizza_c[ingrediente - 1]}")
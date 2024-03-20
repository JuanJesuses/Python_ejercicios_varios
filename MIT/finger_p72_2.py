""" Finger exercise: Write a program that asks the user to enter an
integer and prints two integers, root and pwr, such that 1 < pwr < 6
and root**pwr is equal to the integer entered by the user. If no such
pair of integers exists, it should print a message to that effect. """

import math

user_number = int(input("Enter an integer number: "))

root = round((math.sqrt(user_number)),2)
pwr = user_number**2
producto = round((root**pwr),2)

print(f'La raíz de {user_number} es {root}, la potencia es {pwr} y la potencia de la raíz por la potencia es {producto}')
x,y,z = 9,4,7

if x%2 != 0:
    answer = x
if y%2 != 0 and y > answer:
    answer = y
if z%2 != 0 and z > answer:
    answer = z

print("El mayor número impar de los tres es:", answer)

print("El mayor número impar de los tres es:",(x if x > y else y) if x > z else (y if y > z else z))
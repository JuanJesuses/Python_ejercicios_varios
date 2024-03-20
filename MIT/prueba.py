x = int(input("Enter a number: "))
smallest_divisor = None

if x % 2 == 0:
    smallest_divisor = 2
else:
    for guess in range(3,x,2):
        if x % guess == 0:
            smallest_divisor = guess
            break

if smallest_divisor != None:
    print(f'Smallest divisor of {x} is {smallest_divisor}')
else:
    print(f'{x} is a prime number')

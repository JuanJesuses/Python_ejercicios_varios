x = 3
xans = 0

for num_iterations in range(abs(x)):
    xans = xans + x

print(f'{x} * {x} = {xans}')

x = 1
for i in range(x):
    print(i)
    x = 4

x = 3

for j in range(x):
    print('Iteration of outer loop.')
    for i in range(x):
        print('    Iteration of inner loop.')
        x = 2

total = 0

for c in '12345678':
    total = total + int(c)

print(total)

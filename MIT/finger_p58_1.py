# Finger exercise: Replace the comment in the following code with a while loop.

num_x = int(input('How many times should I print the letter X? '))
to_print = ''

while num_x > 0:
    to_print = to_print + 'x'
    num_x -= 1

print(to_print)
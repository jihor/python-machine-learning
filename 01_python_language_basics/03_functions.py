def add_numbers(x, y):
    return x + y
    (x, y, z)

a = 1
b = 3
c = add_numbers(a, b)
print("{} + {} = {}".format(a, b, c))

from supplemental_functions import add_three_numbers

d = 5
e = add_three_numbers(a, b, d)
print("{} + {} + {} = {}".format(a, b, d, e))
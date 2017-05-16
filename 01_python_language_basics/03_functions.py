def add_numbers(x, y):
    return x + y
    (x, y, z)

a = 1
b = 3
x = add_numbers(a, b)
print("{} + {} = {}".format(a, b, x))

# redefines existing function
from supplemental_functions import add_numbers

c = 5
y = add_numbers(a, b, c)
# add_numbers(a, b) would've thrown an error now
print("{} + {} + {} = {}".format(a, b, c, y))

# redefines existing function again
def add_numbers(x, y, z = 0, printout = False):
    if printout == True:
        print("adding {} and {} to {}".format(z, y, x) if z != 0 else "adding {} to {}".format(y, x))
    return x + y + z

z = add_numbers(a, b)
print("{} + {} = {}".format(a, b, z))
z = add_numbers(a, b, c)
print("{} + {} + {} = {}".format(a, b, c, z))
z = add_numbers(a, b, c, True)
print("{} + {} + {} = {}".format(a, b, c, z))
# arguments are bound positionally, not by type, so True is treated as 1
z = add_numbers(a, b, True)
print("{} + {} + {} = {}".format(a, b, True, z)) # 1 + 3 + True = 5

# arguments can be bound by name
z = add_numbers(a, b, printout=True)             # "adding 3 to 1"
print("{} + {} = {}".format(a, b, z))
z = add_numbers(printout=True, x=a, y=b, z=c)    # "adding 5 and 3 to 1"
print("{} + {} + {} = {}".format(a, b, c, z))

# event "x=x" constructs evaluate correctly
x = 7; y = 8; z = 9                              # multiple operations on one string
r = add_numbers(printout=True, x=x, y=y, z=z)    # "adding 9 and 8 to 7"
print("{} + {} + {} = {}".format(x, y, z, r))


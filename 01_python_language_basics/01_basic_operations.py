# this is a comment
"""
   this is a multiline (documentation-style
   comment
"""

print('------------\nHello, is this the future?')   # no difference between " and '
print("Python code style is defined in PEP 8\n------------")

# Assignments
print("\nAssignments")
a = 7
b = a + 1
c = a - 1
d = a * 2
e = a / 2
f = a ^ 2
print(a, b, c, d, e, f)

# Equality comparisons
print("\nEquality comparisons")
print(1 == 1)    # True and False start with capital letter
print(1 != 1)

# Logical operators
print("\nLogical operators")
print(3 and 5)   # 5 - 'and' is a normal 'and' and returns the last arg
print(4 or 2)    # 4 - 'or' is a normal 'or' and returns first non-zero arg
# Beware of these:
print(3 & 6)     # 2 - '&' is a bitwise 'and'
print(2 | 1)     # 3 - '|' is a bitwise 'or'

# Rounding
print("\nRounding")
x = 0.125
print(round(x, 2))  # 0.12 - default rounding works round half down
y = 0.126
print(round(y, 2))  # 0.13

# Help
print("\nUsing help")
help(round)
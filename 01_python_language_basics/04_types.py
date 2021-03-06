def a():
    pass                            # pass is a no-op for when an operation is syntactically required

print("Functions")
print(type(a))                      # <class 'function'>
print(type(lambda x: None))         # <class 'function'>

# Strings can be enclosed in single or double quotes, there is no difference
print("\nStrings")
print(type('a'))       # <class 'str'>
print(type("a"))       # <class 'str'>
print("'a' == ", '"a"', " -> {}".format('a' == "a"))   # True
s = "Some nice"
print(s + " flowers")
# Strings can be traversed and sliced like arrays
for letter in s:
    print(letter)
print(s[0:3])          # range [0, 3)
# Strings are immutable
try:
    s[0] = "x"
except Exception as e:
    print(e)
print('"Mike" in "Mike Smith" -> {}'.format("Mike" in "Mike Smith"))  # True
print('"miKe" in "Mike Smith" -> {}'.format("miKe" in "Mike Smith"))  # False
# numeric types must be converted to string for concatenation to work
try:
    print ("sk" + 8 + "er")
except Exception as e:
    print(e)                    # must be str, not int
print ("sk" + str(8) + "er")    # sk8er
# split()
x = "Hello world".split()
print(x)                        # ['Hello', 'world']
x = "Hello, world".split(", ")
print(x)                        # ['Hello', 'world']

# Numeric types
print("\nNumeric types")
print(type(1))         # <class 'int'>
print(type(1.0))       # <class 'float'>
print(type(float(1)))  # <class 'float'>

# Boolean type
print("\nBoolean type")
print(type(True))      # <class 'bool'>
print(type(False))     # <class 'bool'>

# 'None' is how null value looks in Python
print("\n'None' type")
print(type(None))      # <class 'NoneType'>

# Tuples are first-class citizens
print("\nTuples")
print(type((1, 2, 3))) # <class 'tuple'>
print(type((1, "a", None)))         # <class 'tuple'>

# Tuples are immutable
a = (1, 2, 3)
x, y, z = a
print(x, y, z)   # 1 2 3

print(list(a))                # [1, 2, 3] - will work on any iterable
print(set((1, 2, 2, 1, 3)))   # [1, 2, 3] - will work on any iterable

try:
    a[0] = -1
except Exception as e:
    print(e)
ar = reversed(a)
print(a)      # (1, 2, 3)
print(ar)     # <reversed object at 0x000000621965A2E8>
for i in ar:
    print(i)

# Lists are defined using []
print("\nLists")
l = [1, "a", 3]
x, y, z = l
print(x, y, z)     # 1 a 3
print(l)           # [1, 'a', 3]
print(type(l))     # <class 'list'>
print(3 * l)       # lists can be repeated
print([1] * 33)    # lots of ones
print([1, 2] + [3, 4])    # lists support '+' and '+=' operations
print("2 in [1, 2, 3] -> {}".format(2 in [1, 2, 3]))

# lists are mutable
l[0] = 8
l[1] = None
l.append("horse")
l += "bzix"  # Will iterate over string (it behaves like a list, remember?) and add every element to list.
             # But there is no "-=" operation
print(l)     # [8, None, 3, 'horse', 'b', 'z', 'i', 'x']
l.remove("b")
l.remove(8)
print(l)     # [None, 3, 'horse', 'z', 'i', 'x']
l.reverse()  # does in-place reverse - lists are mutable
print(l)     # ['x', 'i', 'z', 'horse', 3, None]

# slicing lists
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[0:3])    # range [0 .. 3) -> [0, 1, 2]
print(a[-1])     # 1st from end -> 9
print(a[-4:-1])  # range [4th from end .. 1st from end) -> [6, 7, 8]
print(a[-4:])    # range [4th from end .. end]  -> [6, 7, 8, 9]
print(a[:-4])    # range [start .. 4th from end) -> [0, 1, 2, 3, 4, 5]
print(a[:-4:2])  # range [start .. 4th from end), step = 2 -> [0, 2, 3]

# dictionaries are defined with {}
print("\nDictionaries")
d = {1: "a", "b": 2}
print(type(d))       # <class 'dict'>
# dictionaries are mutable
print(d)
d[1] = 'e'
d["b"] = 3
d["x"] = None
print(d)
d2 = {"x": 123, "y": 16}
# no sugar for dicts
try:
    d = d + d2
except Exception as e:
    print(e)

try:
    d += d2
except Exception as e:
    print(e)


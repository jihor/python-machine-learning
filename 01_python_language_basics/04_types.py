def a():
    None

print(type(a))                      # <class 'function'>
print(type(lambda x: None))         # <class 'function'>

print(type('a'))                    # <class 'str'>
print(type("a"))                    # <class 'str'>
print(type(1))                      # <class 'int'>
print(type(1.0))                    # <class 'float'>
print(type(True))                   # <class 'bool'>
print(type(False))                  # <class 'bool'>
# 'None' is how null value looks in Python
print(type(None))                   # <class 'NoneType'>
# Tuples are first-class citizens
print(type((1, 2, 3)))              # <class 'tuple'>
print(type((1, "a", None)))         # <class 'tuple'>
# lists are defined with []
print(type([1, "a", 3]))            # <class 'list'>
# dictionaries are defined with {}
print(type({1: "a", "b": 2}))       # <class 'dict'>


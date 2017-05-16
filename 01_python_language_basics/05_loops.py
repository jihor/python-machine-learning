x = [1, "a", 2]

print("Iterate over list")
for item in x:
    print(item)

y = {1: "val1", "b": 263}

# simple 'in' iterates over keys for dictionary
print("\nIterate over dict keys")
for k in y:
    print(k)

# same
print("Iterate over dict keys again")
for k in y.keys():
    print(k)

# iterate over values
print("\nIterate over dict values")
for v in y.values():
    print(v)

# iterate over pairs (was "iteritems()" in Python 2)
print("\nIterate over dict pairs")
for pair in y.items():
    print(pair)
print()

# Iterate over keys with index
print("\nIterate over keys with index")
for number, k in enumerate(y):
    print("Key {} is {}".format(number, k))

# Iterate over multiple iterables
print("\nIterate over multiple arrays")
# ends with the shortest iterable ending
for a, b in zip(range(10, 60, 10), range(10)):
    print(a + b)

# Simple while loop
print("\nSimple while loop")
i = 0
while i < len(x):
    print(x[i])
    i += 1


# strings are lists in Python
# this loop will print 'smNc'
print("\nFor-loop over a string")
for l in 'SomeNice624':
    if l in "aeiouy":
        continue
    if l.isnumeric():
        break
    print(l)

# List comprehensions are special one-line-style loops
print("\nList comprehensions")
# ok up to 100, but will produce wrong results starting with 121, which is 11*11
noprimes = [j for i in (2, 3, 5, 7) for j in range(i*2, 100, i)]
primes = [x for x in range(2, 100) if x not in noprimes]
print(primes)

print([a for a in range(10) if a % 2 == 1])
print(sorted(set([(a*b*c*d) for a in range(1, 4) for b in range(1, 4) for c in range(1, 4) for d in range(1, 4)])))


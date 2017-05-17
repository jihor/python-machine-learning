import numpy as np

# NumPy basics
print("NumPy basics")
n = np.array([1, 2, 3])
print(type(n))          # <class 'numpy.ndarray'>
print(n)                # [1, 2, 3]
print(n.astype(float))  # [ 1.  2.  3.]

m = np.array([[1, 2], [3, 4], [5, 6]])   # 3*2 matrix
print(m)
print(m.shape)         # (3, 2)

print("\nndarray.reshape() and resize()")
print("reshape -> \n", m.reshape(2, 3))  # only changes the view, returns view
print("m is still -> \n", m)            # m is still 3*2
print("resize -> \n", m.resize(3, 3))    # changes the object itself, pads with zeroes, returns None
print("mi is now -> \n", m)             # m is 2*3 now

print("\nnumpy.reshape() and resize()")
m = np.array([[1, 2], [3, 4], [5, 6]])          # 3*2 matrix
print("reshape -> \n", np.reshape(m, (2, 3)))   # only changes the view, returns view
print("m is still \n", m)                       # m is still 3*2
print("resize -> \n", np.resize(m, (3, 3)))     # returns changed copy, pads with copied values
print("m is still \n", m)                       # m is still 3*2

# Generating matrices
print("\nGenerating matrices")
m = np.arange(0, 10, 2)    # [0 .. 10) range with step 2
print(m)
m = np.linspace(0, 10, 5)  # 5 evenly spaced values in [0 .. 10] range
print(m)
print(np.ones((3, 2)))
print(np.ones((3, 2), int))
print(np.zeros((3, 2)))
print(np.zeros((3, 2), int))
print(np.diag(np.array([1, 2, 3])))
print("identity matrices")
print(np.eye(3))
print(np.eye(3, dtype=int))
print(np.eye(3, 2, dtype=int))
print(np.eye(3, 4, 1, int))

# Slicing matrices works like with array and strings
print("\nSlicing matrices")
m = np.array([[1, 2, 3], [10, 20, 30], [100, 200, 300], [1000, 2000, 3000], [10000, 20000, 30000]])
n = np.array([2, 4, 6])
print(m)
print(m[::2, 0:2])

print("\nMatrix operators")
print(m < 150)       # returns matrix of comparison results
print(m + m)        # element-wise sum
print(m - m)        # element-wise subtraction
print(3 * m)        # element-wise multiplication
print(m * 3)        # same
print(m * m)        # same
print(m / 3)        # element-wise division
print(3 / m)        # same
print(m / m)        # same
print(m // 3)       # element-wise floor division
print(m % 100)      # element-wise division remai   nder
print(m ** 2)       # element-wise exponent
# beware:
print("'^' operator is not the exponent - it's element-wise bitwise binary XOR")
print(m ^ 2)        # not the exponent - it's element-wise bitwise binary XOR

print("\nMatrix dot product")
print(m.dot(n))     # matrix doc product, (M,N) * (N*K) -> (M,K)
print("\nMatrix transposition")
print(m.T)

print("\nMatrix row-wise stacking")
a1 = np.arange(6.0).reshape(2, 3).astype(int)
a2 = np.array([['a', 'b', 'c'], ['d', 'e', 'f']])
print(np.vstack((a1, a2)))
print(np.concatenate((a1, a2), axis=0))
print("\nMatrix column-wise stacking")
print(np.hstack((a1, a2)))
print(np.concatenate((a1, a2), axis=1))
print("\nMatrix row-wise splitting")
a, b = np.vsplit(a1, 2)
print("a and b are \n{}, and \n{}".format(a, b))
a, b, c = np.vsplit(a1.reshape(3, 2), 3)
print("a, b and c are \n{}, \n{} and \n{}".format(a, b, c))
a, b, c = np.split(a1.reshape(3, 2), 3, axis=0)  # same
print("\nMatrix column-wise splitting")
a, b = np.hsplit(a1.reshape(3, 2), 2)
print("a and b are \n{}, and \n{}".format(a, b))
a, b, c = np.hsplit(a1, 3)
print("a, b and c are \n{}, \n{} and \n{}".format(a, b, c))
a, b, c = np.split(a1.reshape(2, 3), 3, axis=1)  # same

print("\nMatrix statistic functions")
print(m.max())      # not the row, only the element
print(m.min())      # not the row, only the element
print(m.mean())
print(m.sum())
print(m.std())      # standard deviation

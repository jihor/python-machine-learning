[]# 'pip install numpy' will install numpy
import numpy

# Defining matrices
print("\nDefining matrices")
A = numpy.matrix('1 2; 3 4; 5 6')   # 3*2 matrix
print("A = ", A)

import numpy as np     # import and alias for convenience
print(np.size(A))      # 6
print(np.size(A, 0))   # 3 - matrix indexes start with 0
print(np.size(A, 1))   # 2
print(np.alen(A))      # 3

# Sizes and selections
print("\nMatrix sizes and selections")
print(A[0, :])    # [1 2] - 1st column, all rows
print(A[:, 1])    # [2; 4; 6] - all columns 2nd row

B = np.matrix('1 2 3 4; 10 20 30 40; 100 200 300 400; 1000 2000 3000 4000; 10000 20000 30000 40000')   # 5*4 matrix
print(B[0::3, :])  # from 1st row with row step 3, all columns
C = np.matrix('9 91 93 95')
B[0] = C
B[4, 0:2] = np.matrix('0 0')
print(B)

# Matrix operations
print("\nMatrix operations")
D = np.matrix('1, 2; 3, 4; 5, 6')       # comma may be present
E = np.matrix('10 20; 30 40; 50 60')    # or absent between line elements
F = np.matrix('1 2; 2 4')
print(np.concatenate((D, E)))           # concatenate adding rows
print(np.concatenate((D, E), axis=0))   # same
print(np.concatenate((D, E), axis=1))   # concatenate adding columns
print(np.dot(D, F))      # [  5  10;  11  22;  17  34] - usual matrix multiplication, where MxN * NxL -> MxL
print(np.dot(D, 5))      # [  5  10;  15  20;  25  30]
print(np.multiply(D, E)) # [ 10  40;  90 160; 250 360] - element-wise multiplication. Matrices must have the same dimensions
print(np.multiply(D, 5)) # [  5  10;  15  20;  25  30]
print(np.divide(D, 10))  # [0.1 0.2; 0.3 0.4; 0.5 0.6]
print(np.divide(D, E))   # [0.1 0.1; 0.1 0.1; 0.1 0.1] - element-wise division, left arg over right arg. Matrices must have the same dimensions

# Solving simple equations
print("\nSolving AxB = C equations")
# np.linalg.solve searches for exact solution and will not compute here.
# Using np.linalg.lstsq
# This is an equivalent of Matlab's A \ b
b = np.matrix('4; 10; 16')
x, resid, rank, s = np.linalg.lstsq(A, b)
print(x)   # [2; 1] - returns T for AxT = b equation. I.e. T = inv(A)*b
# NumPy has no direct equivalent to Matlab's A / b
# We should then solve x.T * A.T = b.T instead. Then A.T = x.T \ b.T
a, resid, rank, s = np.linalg.lstsq(x.T, b.T)
print(a.T)   # [1.6 0.8;   4   2; 6.4 3.2] * [2; 1] = [4; 10; 16]
             # and
             # [  1   2;   3   4;   5   6] * [2; 1] = [4; 10; 16]
             # so the result depends on solution search algorithm

# Matrix mutations
print("\nMatrix mutations")
print(A.T)               # transposition
print(np.flipud(A))      # flip the matrix
print(np.linalg.pinv(A)) # pseudo-inverse
print(np.invert(A))      # it's not an inverse matrix - numpy.inverse() will
                         # compute bitwise 'not' with each element of the provided matrix
print(A.flatten())       # flatten matrix to a vector

# Matrix statistic functions
print("\nMatrix statistic functions")
print(np.max(A))  # 6
print(np.max(A, 0))  # [5 6] - row with the max element
print(np.max(A, 1))  # [2; 4; 6] - column with the max element
print(np.max(A[:]))  # [2; 4; 6] - column with the max element
print(B < 300)             # matrix of the same size, filled with true / false
print(sum(B))              # row-wise sum
print(np.sum(B))           # 81388 - sum of all elements
print(np.sum(B, axis=0))   # [1119 2311 33423 44535] - row-wise sum
print(np.sum(B, axis=1))   #  - column-wise sum
print(np.prod(A))          # 720 - product of matrix elements
print(np.prod(A, axis=0))  # [15 48] - column-wise product
print(np.prod(A, axis=1))  # [2; 12; 30] - row-wise product

# Matrix generation functions
print("\nMatrix generation functions")
print(np.ones((3, 2)))          # matrix of ones
print(np.ones((3, 2), int))     # matrix of ones as ints
print(np.ones((3, 2), np.int))  # same
print(np.zeros((3, 2)))         # matrix of zeros
print(np.zeros((3, 2), int))    # matrix of zeros as ints
print(np.zeros((3, 2), np.int)) # same
print(np.eye(3))                # identity matrix
print(np.eye(3, dtype=int))     # identity matrix as ints
print(np.arange(1, 5))          # [a .. b) range, produces [1 2 3 4]
print(np.arange(1, 5, 0.5))     # [a .. b) range with step 0.5, produces [1  1.5  2  2.5  3  3.5  4  4.5]
print(np.random.rand(3, 2))   # 3x2 matrix of random-distributed values in [0..1] range
                              # (uniform distribution)
print(np.random.randn(3, 2))  # 3x2 matrix of random-distributed values
                              # (normal / gaussian distribution with mean value = 0 and variance = 1)
G = np.histogram(np.random.randn(1, 100), bins=100)
print(G)
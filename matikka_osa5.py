import numpy as np
import sympy as sp

x = sp.symbols('x')
#1a)
A = np.array([[-1, 2], [3, 1]])
B = np.array([[0, 1, 3], [2, -3, 5]])

result1a = np.dot(A, B)
print(result1a)

#1b)
C = np.array([[1, 3, 5], [0, -2, 1], [2, -1, 4]])
D = np.array([[1], [-3], [-1]])

result1b = np.dot(C, D)
print(result1b)

E = np.array([[2, 0, 1], [1, -3, 4], [0, 1, 5]])
F = np.array([[3], [-5], [7]])

result1c = np.dot(E, F)
print(result1c)

G = np.array([[1, -4, 2], [3, 0, -2], [2, 1, 0]])
H = np.array([[5, 1, -1], [-2, 1, 3], [0, 3, 4]])

result1d = np.dot(G, H)
print(result1d)

#osa5 tehtävät, 1

I = np.array([[4, 9, 0], [-3, 7, -11]])
print(np.transpose(I))

J = np.array([[8, 9], [-3, 12], [0, -1], [7, 1]])
print(np.transpose(J))

#2
K = np.array([[5, -6], [8, 10]])
print(np.linalg.det(K))

L_sympy = sp.Matrix([[1 - x, -x], [x, 1 - x]])
det = L_sympy.det()
print(det)

M = np.array([[2, 3, 4], [-2, -1, 1], [5, 3, 2]])
print(np.linalg.det(M))

N = np.array([[3, 15, 7], [0, -4, 0], [3, 2, 3]])
print(np.linalg.det(N))

#3. 1.

O = np.array([[-2, 0, 8, 5], [3, -1, 2, 1], [4, 7, 6, 2], [1, 0, 2, 3]])
print(np.linalg.det(O))
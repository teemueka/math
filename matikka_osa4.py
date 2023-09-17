import sympy as sp
from sympy import Eq, symbols

#osa2, 1 ja 2 kohdasta 1

x, y, z = symbols('x y z')

eq1 = Eq(x - 2*y - 2*z, 0)
eq2 = Eq(-2*x + y - z, -3)
eq3 = Eq(3*x + 2*y + z, 4)

solution1A = sp.solve((eq1, eq2, eq3), (x, y, z))
print("1. a) ", solution1A)

eq4 = Eq(x + y, 1)
eq5 = Eq(2*x + y - z, 1)
eq6 = Eq(3*x + y - 2*z, 1)

solution1B = sp.solve((eq4, eq5, eq6), (x, y, z))
print("1. b) ", solution1B)

eq7 = Eq(2*x + 4*y - z, 11)
eq8 = Eq(6*x - y - 3*z, 7)
eq9 = Eq(4*x + 5*y - 2*z, 16)

solution2A = sp.solve((eq7, eq8, eq9), (x, y, z))
print("2. a) ", solution2A)

eq10 = Eq(4*x + 2*y - 2*z, 0)
eq11 = Eq(2*x + y - z, 1)
eq12 = Eq(3*x + y - 2*z, 1)

solution2B = sp.solve((eq10, eq11, eq12), (x, y, z))
print("2. b) ", solution2B)

#osa3 kertaukset

eq13 = Eq(5*x + 3*y, 9)
eq14 = Eq(2*x + y, 4)

solutionKertaus1A = sp.solve((eq13, eq14), (x, y))
print("1. a) ", solutionKertaus1A)

eq15 = Eq(2*x + y + z, 6)
eq16 = Eq(x + 3*y + z, 2)
eq17 = Eq(2*x + y + 2*z, 9)

solutionKertaus1B = sp.solve((eq15, eq16, eq17), (x, y, z))
print("1. b) ", solutionKertaus1B)

eq18 = Eq(x + y + 3*z, -1)
eq19 = Eq(3*x + y + z, 5)
eq20 = Eq(2*x + y + 2*z, 2)

solutionKertaus1C = sp.solve((eq18, eq19, eq20), (x, y, z))
print("1. c) ", solutionKertaus1C)
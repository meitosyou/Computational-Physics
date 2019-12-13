from sympy import *

x,y = symbols('x y')

a = sin(x).series(x,10)
print(a)

b = sin(x).series(x,0)
print(b)

z = 1/cos(x)
print(z)

w = z.series(x,0)
print(w)

v = z**8
print(v)

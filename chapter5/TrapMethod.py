from numpy import *

def func(x):
    return 5 * (sin(8*x))**2*exp(-x**2) -13*cos(3*x)

def trapezoid(A,B,N):
    h = (B - A)/(N - 1)
    sum = (func(A) + func(B))/2
    for i in range(1, N-1):
        sum += func(A+i*h)
    return h * sum

A = 0.5
B = 2.3
N = 1200
print(trapezoid(A,B,N-1))

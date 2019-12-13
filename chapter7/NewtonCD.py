from math import cos

x =4
dx = 3e-1
eps = 0.2
imax = 100

def f(x):
    return 2 * cos(x) - x

for it in range(0, imax + 1):
    F = f(x)
    if( abs(F) <= eps):
        print("\n Root found , F =", F, ", tolerance eps = ", eps)
        break
    print("Iteration # = ", it,"x = ", x, "f(x) = ", F)
    df = (f(x+dx/2) - f(x-dx/2))/dx
    dx = -F/df
    x += dx


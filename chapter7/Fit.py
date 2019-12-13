import pylab as plt
from numpy import *
from numpy.linalg import inv
from numpy.linalg import solve

t = arange(1.0 , 2.0 , 0.1)
x = array([1. , 1.1 , 1.24 , 1.35 , 1.451 , 1.5 , 1.92])
y = array([0.52 , 0.8 , 0.7 , 1.8 , 2.9 , 2.9 , 3.6])
plt.plot(x,y,'bo')
sig = array([0.1 , 0.1 , 0.2 , 0.3 , 0.2 , 0.1 , 0.1])
plt.errorbar(x, y, sig)
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.grid(True) #目盛りを入れる
Nd = 7
A = zeros((3,3) ,float)
bvec = zeros((3,1),float)
ss = sx = sxx = sxx = sxxx = sxxx = sxxxx = 0
sxy = sxxy = sy = 0

for i in range(0, Nd):
    sig2 = sig[i]**2
    ss += 1.0 / sig2
    sx += x[i]/ sig2
    sy += y[i]/ sig2
    rhl = x[i]**2
    sxx +=rhl/sig2
    sxxy += rhl*y[i]/sig2
    sxy += x[i]*y[i]/sig2
    sxxx += rhl*x[i]/sig2
    sxxxx += (rhl**2)/sig2

A = array([[ss,sx,sxx],[sx,sxx,sxxx],[sxx,sxxx,sxxxx]])
bvec = array([sy,sxy,sxxy])

xvec = dot(inv(A), bvec)
ltest = dot(A , inv(A))
print('\n Matrix via direct')
print(xvec, 'end=')
print('A*inverse(A)')
print(ltest ,'\n')
xvec = solve(A , bvec)
print('x Matrix via direct')
print(xvec, 'end=')
print('FitParabola Final Results \n')
print('y(x) = a0+a1*x+a2*(x**2)')
print('a0 = ', x[0])
print('a1 = ', x[1])
print('a2 = ', x[2] , '\n')
print('i   xi    yi    yfit')

for i in range(0, Nd):
    s = xvec[0] + xvec[1]*x[i] + xvec[2]*(x[i]**2)
    print("%d %5.3f %5.3f %8.7f \n" %(i , x[i], y[i], s))

curve = xvec[0] + xvec[1]*t + xvec[2]*t**2
points = xvec[0] + xvec[1]*x + xvec[2]*x**2
plt.plot(t, curve ,'r',  x, points,'ro')    

plt.show()

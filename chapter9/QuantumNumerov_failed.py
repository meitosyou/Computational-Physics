from numpy import *
import matplotlib.pyplot as plt



dl    = 1e-6                      # very small interval to stop bisection
ul    = zeros([1501], float)
ur    = zeros([1501], float)
k2l   = zeros([1501], float)                        # k**2 left wavefunc
k2r   = zeros([1501], float)                         
n     = 1501
m     = 5                                           # plot every 5 points
imax  = 100 
xl0   = -1000
xr0   =  1000                    # leftmost, rightmost x  
h     = 1.0*(xr0-xl0)/(n-1.)            
amin  = -0.001
amax  = -0.00085                            # root limits
e     = amin                                            # Initial E guess
de    = 0.01
ul[0] = 0.0
ul[1] = 0.00001
ur[0] = 0.0
ur[1] = 0.00001     
im = 500                                                    # match point
nl = im+2
nr = n-im+1                                # left, right wv
istep=0


def V(x):                                                   # Square well
    if (abs(x)<=500):	  v = -0.001                            
    else:               v = 0
    return v

def setk2():                                                       #  k2  
    for i in range(0,n):         
       xl = xl0+i*h
       xr = xr0-i*h
       k2l[i] = e-V(xl)
       k2r[i] = e-V(xr)
			 
def numerov (n,h,k2,u):                             # Numerov algorithm  
    b=(h**2)/12.0                          
    for i in range(1, n-1):  
     u[i+1] = (2*u[i]*(1-5*b*k2[i])-(1.+b*k2[i-1])*u[i-1])/(1+b*k2[i+1])
				
setk2()
numerov (nl, h, k2l, ul)                                       # Left psi
numerov (nr, h, k2r, ur)                                      # Right psi
fact= ur[nr-2]/ul[im]                                             # Scale
for i  in range (0,nl): ul[i] = fact*ul[i]
f0 = (ur[nr-1]+ul[nl-1]-ur[nr-3]-ul[nl-3])/(2*h*ur[nr-2])    #  Log deriv

"""

while abs(de)>dl and istep < imax:
    e1 = e
"""
fig1 = plt.figure(1, figsize=(6,6))
plt.title('RK4')
plt.xlabel('t')
plt.ylabel('Y[0]')
plt.plot(xlist,y1list,marker='o',color = 'blue')

fig2 = plt.figure(2, figsize=(6,6))
plt.title('RK4')
plt.xlabel('t')
plt.ylabel('Y[1]')
plt.plot(xlist,y2list,marker='o',color = 'red')

plt.show()

    

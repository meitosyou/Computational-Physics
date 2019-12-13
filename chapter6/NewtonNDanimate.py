from numpy import *
import matplotlib.pyplot as plt
from numpy.linalg import solve
import matplotlib.animation as animation
import matplotlib.patches as patches

n = 9
eps = 1e-3
deriv = zeros((n,n),float)
f = zeros((n),float)
x = array([0.5 , 0.5 , 0.5 , 0.5 , 0.5 , 0.5 , 1.0 , 1.0 , 1.0])


#ims =[]
fig = plt.figure()
plt.title('String and masses configuration')


def plotconfig():
    patches.Circle(xy=(0,0), radius=0.5)

def F(x, f):
    f[0] = 3*x[3] + 4*x[4] +4*x[5] -8.0
    f[1] = 3*x[0] + 4*x[1] -4*x[2]
    f[2] = x[6]*x[0] - x[7]*x[1] -10.0
    f[3] = x[6]*x[3] - x[7]*x[4]
    f[4] = x[7]*x[1] + x[8]*x[2] -20.0
    f[5] = x[7]*x[4] - x[8]*x[5]
    f[6] = pow(x[0], 2) + pow(x[3], 2) - 1.0
    f[7] = pow(x[1], 2) + pow(x[4], 2) - 1.0
    f[8] = pow(x[2], 2) + pow(x[5], 2) - 1.0
    
def dFi_dXj (x, deriv , n):
    h = 1e-4
    for j in range(0,n):
        temp = x[j]
        x [j] += h/2
        F(x,f)
        for i in range(0, n):
            deriv[i,j] = f[i]
        x[j] = temp
    for j in range(0,n):
        temp = x[j]
        x[j] -= h/2
        F(x,f)
        for i in range(0,n):
            deriv[i,j] = (deriv[i,j] - f[i])/h
        x[j] = temp

for it in range(1,100):
    F(x,f)
    dFi_dXj(x, deriv, n)
    B = array([[-f[0]], [-f[1]], [-f[2]], [-f[3]], [-f[4]], [-f[5]], [-f[6]], [-f[7]], [-f[8]]])
    sol = solve(deriv , B)  # Δｘを求める
    dx = take(sol, (0, ), 1)
    for i in range(0,n):
        x[i] = x[i] + dx[i]
    ims = plotconfig()
    #im = plotconfig()
    #ims.append(im)
    errX = errF = errXi = 0.0
    for i in range(0,n):
        if(x[i] != 0.0):
            errXi = abs(dx[i]/x[i])
        else:
            errXi = abs(dx[i])
        if(errXi > errX):
            errX = errXi
        if(abs(f[i]) > errF):
            errF = abs(f[i])
        if((errX <= eps) and (errF <= eps)):
            break

print("Number of iterations =", it , "\n Final Solution:")
for i in range(0, n):
    print('x[', i ,'] = ' , x[i])

ani = animation.ArtistAnimation(fig,ims,interval=100)
#ani.save('test1.gif', writer='imagemagick')
plt.show()


"""
まだ絵を出せていない！！
"""

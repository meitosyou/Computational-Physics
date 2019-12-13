
import math
import numpy as np
from matplotlib import pyplot as plt

Xmax = 40
Xmin = 0.25
step = 0.1
order = 10
start = 50

fig = plt.figure()
plt.title('Special Bessel')
plt.xlabel('x')
plt.ylabel('j(x)')
plt.xlim(Xmin, Xmax)
plt.ylim(-0.2 , 0.5)

def down (x, n, m):
    j = np.zeros( (start + 2) , float)
    j[m+1] =j[m] = 1
    for k in range(m, 0, -1):
        j[k-1]=((2.0*k + 1.0)/x)*j[k] - j[k+1]    #this is (3.25)
    scale = (np.sin(x) / x)/j[0]
    return j[n] * scale

x1 = np.arange(Xmin, Xmax, step)
y1 = [down(x,order, start) for x in x1]
plt.plot(x1, y1, 'green')

x2 = np.arange(Xmin, Xmax, step)
y2 = [down(x ,1, start) for x in x2]
plt.plot(x2, y2, 'red')

plt.show()

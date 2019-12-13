import numpy as np
import matplotlib.pyplot as plt

N = 100
x1 = np.arange(0, 2*np.pi + 2*np.pi/N , 2*np.pi/N)
fig , ax = plt.subplots()
y1 = x1 * np.sin(x1) **2
ax.plot(x1, y1, 'c', linewidth = 4)
ax.set_xlim((0, 2 * np.pi))
ax.set_ylim((0, 5))
ax.set_xticks([0, np.pi , 2*np.pi])
#ax.set_xticklabels(['0', '$\uppi$', '2$\uppi$'])
ax.set_xticklabels(['0','pi','2*pi'])
ax.set_ylabel('$f(x) = x\. \sin^2 x$', fontsize = 20)
ax.set_xlabel('x', fontsize = 20)
fig.patch.set_visible(False)
xi=[]
yi=[]
xo=[]
yo=[]

def fx (x):
    return x * np.sin(x)**2

j = 0
Npts = 3000
analyt =np.pi **2
xx = 2 * np.pi *np.random.rand(Npts)
yy = 5 * np.random.rand(Npts)
for i in range(1,Npts):
    if (yy[i] <= fx(xx[i])):
        if (i <=100):
            xi.append(xx[i])
        if (i <=100):
            yi.append(yy[i])
        j +=1

    else:
        if (i <=100):
            xo.append(xx[i])
        if (i <=100):
            yo.append(yy[i])

    boxarea = 2 *np.pi *5
    area = boxarea* j /(Npts -1)
    ax.plot(xo ,yo ,'bo', markersize = 3)
    ax.plot(xi ,yi ,'ro', markersize = 3)
    ax.set_title('Answers:  Analytic = %5.3f, MC = %5.3f' %(analyt, area))

plt.show()

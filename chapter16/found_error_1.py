
import matplotlib.pyplot as plt
from numpy import *
import matplotlib.animation as animation

xlist = []
ylist = []
def init():
    for j in range(0,50):       
        for i in range(0,50):
            xx = i+j
            yy = i-j
            xlist.append(xx)
            ylist.append(yy)

init()

fig=plt.figure()                            
ax = fig.add_subplot(111, autoscale_on=False,xlim=(-50,50),ylim=(-50,50))
ax.grid()                                                       # Plot  grid
plt.title('Game of Life')




#point, = ax.plot(xx,yy,"r",lw = 2)
point,= ax.plot(xlist,ylist, 'o',lw=2)    
k= range(0, 51)
def animate(dum):
    
    #xlist.clear()
    #ylist.clear()#clearの位置はここ
    for j in range(0,50):       
        for i in range(0,50):
            xx = i+j
            yy = i-j
            #xlist.append(xx)
            #ylist.append(yy)
            point.set_data(xx,k)
    #point, = plt.plot(xlist,ylist, 'o',lw=2)
    #zz = range(1,51)
    #point, = plt.plot(xx,yy, 'o',lw=2)
    #point, = plt.plot(xx,zz,'o',lw=2)
    #point.set_data(xlist,ylist)
    a=1
    b=2
    point.set_data(a,b)
    print(point)  #動いてはいる

    #k+=1
    return point,

ani = animation.FuncAnimation(fig, animate,1)
plt.show()




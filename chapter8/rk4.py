from numpy import *
import matplotlib.pyplot as plt


n = 100
ydumb = zeros((2),float)
y = zeros((2),float)
k1 = zeros((2),float)
k2 = zeros((2),float)
k3 = zeros((2),float)
k4 = zeros((2),float)
fReturn = zeros((2),float)
y[0]=3
y[1]=-5
a =0.0
b = 10.0
t = a
h = (b-a)/n

xlist = []  # x座標
y1list = []  # y座標
y2list = []
#ims = []

def f(t,y):
    fReturn[0] = y[1]
    fReturn[1] = -100*y[0] -2*y[1] + 10*sin(3*t)
    return fReturn

def rk4(t,h,n):
    k1 = [0]*(n)
    k2 = [0]*(n)
    k3 = [0]*(n)
    k4 = [0]*(n)
    fR = [0]*(n)
    ydumb = [0]*(n)
    fR = f(t,y)
    for i in range(0,n):
        k1[i] = h*fR[i]
    for i in range(0,n):
        ydumb[i] = y[i] + k1[i]/2
    k2 = h*f(t+h/2 , ydumb)
    for i in range(0,n):
        ydumb[i] = y[i] + k2[i]/2
    k3 = h*f(t+h/2 , ydumb)
    for i in range(0,n):
        ydumb[i] = y[i] + k3[i]
    k4 = h*f(t+h, ydumb)
    for i in range(0,2):
        y[i] +=  (k1[i] + 2*k2[i] + 2*k3[i] + k4[i])/6
    return y

while(t<b):
    xlist.append(t)
    y1list.append(y[0])
    y2list.append(y[1])
    if ((t+h) > b):
        h = b-t
    y = rk4(t,h,2)
    t += h
    

    #im = plt.plot(xlist, ylist, marker='o', color = 'black')
    #im = plt.scatter(xlist, ylist, marker='yellow', color = 'yellow'
    #ims.append(im)


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
#plt.grid('on')
#ani = animation.ArtistAnimation(fig1,ims,interval=100 ,repeat_delay = 500)
#ani = animation.ArtistAnimation(fig2,ims,interval=100 ,repeat_delay = 500)
                  

plt.show()


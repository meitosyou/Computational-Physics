from pylab import *
#import matplotilb
#from matplotlib.pyplot as plt


Xmin = -5.0
Xmax = +5.0
Npoints = 500

DelX = (Xmax - Xmin)/Npoints

x1 = arange(Xmin, Xmax, DelX)
x2 = arange(Xmin, Xmax, DelX/20)
y1 = -sin(x1) * cos(x1 * x1)
y2 = exp(-x2/4) * sin(x2)

print("\n Now plotting , look for FIgures 1 & 2 on desktop")

figure(1)
subplot(2,1,1)
plot(x1, y1, 'r' , lw =2 )
xlabel('x')
ylabel('f(x)')
grid(True)
subplot(2,1,1)
plot(x2, y2, '-', lw =2)
xlabel('x')
ylabel('f(x)')
title('exp(-x/4) *sin(x)')

figure(2)
subplot(2,1,1)
plot(x1, y1*y1,   'r',lw=2)
xlabel('x')
ylabel('f(x)')

figure(3)
subplot(2,1,2)
plot(x2 , y2 * y2 , '-', lw = 2)
xlabel('x')
ylabel('f(x)')
grid(True)

plt.show()



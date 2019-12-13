import scipy.interpolate as ipl
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.00, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.00 ])
y = np.array([10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7])

xnew =np.linspace(0,1,21)
#print(xnew)
#f_linear = ipl.interp1d(x,y,bounds_error = False)
f_cubic = ipl.interp1d(x,y, kind='cubic', bounds_error = False)

#y1 = f_linear(x)
y2 = f_cubic(xnew)

plt.figure(figsize=(6,6))
plt.title('Spline Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,'o', label='original function')
#plt.plot(x,y1,'k:',label='linear completion',linewidth=4)
plt.plot(xnew,y2,'k--', label='3D spline completion',linewidth =4, alpha=0.7)


plt.show()

""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# Waves2Danal.py: analytical solution of Helmholtz eqn rectangular membrane  

import numpy as np; import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d 

t=0; c=np.sqrt(180./390.)   # speed, tension N/m2, density kg/m2                                    
s5=np.sqrt(5); N=32   

def membrane(t,X,Y):         
    return np.cos(c * s5* t) * np.sin( 2* X)*np.sin(Y)  
      
plt.ion(); fig=plt.figure()             # Interactive on
ax = fig.add_subplot(111, projection='3d')
xs = np.linspace(0,np.pi,32); ys = np.linspace(0,np.pi,32)  # 0->pi    
X, Y = np.meshgrid(xs,ys);  Z = membrane(0, X, Y)    # x,y grid; init Z 
wframe = None
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title('Vibrating Membrane')

for t in np.linspace(0,10,40):         # Total time 10 divided by 40
    oldcol = wframe                                 # Previous frame
    Z = membrane(t,X,Y)                          # Membrane at t !=0
    wframe = ax.plot_wireframe(X,Y,Z)               # Plot wireframe
    if oldcol is not None:                       # Remove old frame
        ax.collections.remove(oldcol)
    plt.draw()                                     # Plot new frame

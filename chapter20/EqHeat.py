""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# EqHeat.py: solves heat equation via finite differences, 3-D plot
 
from numpy import *
import matplotlib.pylab as p
from mpl_toolkits.mplot3d import Axes3D 

Nx = 101
Nt = 9000#3000
Dx = 0.03
Dt = 0.9                                                              
KAPPA = 210.0
SPH = 900.0
RHO = 2700.0 # Conductivity, specf heat, density                                                      
T = zeros( (Nx, 2), float)
Tpl = zeros( (Nx, 31), float)  
                                     
print("Working, wait for figure after count to 10")

for ix in range (1, Nx - 1):
   T[ix, 0] = 100.0             # Initial T
T[0,0] = 0.0
T[0,1] = 0.0# 1st & last T = 0
T[Nx-1,0] = 0.0
T[Nx-1,1] = 0.0
cons = KAPPA/(SPH*RHO)*Dt/(Dx*Dx);                             # constant
m = 1                                                           # counter

for t in range (1, Nt):                                  
   for ix in range (1, Nx - 1):                       
      T[ix, 1] = T[ix, 0] +  cons*(T[ix+1, 0] + T[ix-1, 0] - 2.*T[ix,0])                                                        
   if t%300 == 0 or t == 1:                            # Every 300 steps
        for ix in range (1, Nx - 1, 2):
           Tpl[ix, m] = T[ix, 1]   
        print(m)   
        m = m + 1                        
   for ix in range (1, Nx - 1):
      T[ix, 0] = T[ix, 1] 
x = list(range(1, Nx - 1, 2))                       # Plot alternate pts
y = list(range(1, 30))                       
X, Y = p.meshgrid(x, y)                       

def functz(Tpl):                            
    z = Tpl[X, Y]       
    return z

Z = functz(Tpl)              
fig = p.figure()                                          # Create figure
ax = Axes3D(fig)                                              
ax.plot_wireframe(X, Y, Z, color = 'r')                    
ax.set_xlabel('Position')                                     
ax.set_ylabel('time')
ax.set_zlabel('Temperature')
p.show()                               
print("finished")                               

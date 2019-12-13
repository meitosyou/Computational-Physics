""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation""" 
	 
# WangLandau.py: Wang Landau algorithm for 2-D spin system

""" Author in Java: Oscar A. Restrepo, 
 Universidad de Antioquia, Medellin, Colombia
 Each time fac changes, a new histogrm is generated.
 Only the first Histogram plotted to reduce computational time"""
#from visual import *
#from visual.graph import *

import random
import matplotlib.pyplot as plt
from numpy import *
import matplotlib.animation as animation

L = 8;  N  = (L*L)

"""
# Set up graphics
entgr = gdisplay(x=0,y=0,width=500,height=250,title='Density of States',\
			xtitle= 'E/N', ytitle='log g(E)', xmax=2., xmin=-2.,ymax=45,ymin=0)
entrp    = gcurve(color = color.yellow, display = entgr)
energygr = gdisplay(x=0, y=250, width=500, height=250, title='E vs T',\
        xtitle = 'T', ytitle='U(T)/N', xmax=8.,xmin=0, ymax =0.,ymin=-2.)
energ    = gcurve(color = color.cyan, display = energygr)
histogr  = display(x = 0, y = 500, width = 500, height = 300,\
			 title = '1st histogram: H(E) vs. E/N, corresponds to log(f) = 1')
histo = curve(x = list(range(0, N+1)), color=color.red, display=histogr)
xaxis    = curve(pos = [( - N,  - 10), (N,  - 10)])
minE     = label(text = ' - 2', pos = ( - N + 3,  - 15), box = 0)
maxE     = label(text = '2', pos = (N - 3,  - 15), box = 0)
zeroE    = label(text = '0', pos = (0,  - 15), box = 0)
ticm     = curve(pos = [( - N,  - 10), ( - N,  - 13)])
tic0     = curve(pos = [(0,  - 10), (0,  - 13)])
ticM     = curve(pos = [(N,  - 10), (N,  - 13)])
enr      = label(text = 'E/N', pos = (N/2,  - 15), box = 0)
"""

sp     = zeros( (L, L) )                               # Grid size, spins
hist   = zeros( (N + 1) )
prhist = zeros( (N + 1) )                                    # Histograms
S      = zeros( (N + 1), float)                      # Entropy = log g(E)

x1list =[]
y1list = []
x2list = []
y2list = []
x3list = []
y3list = []
ims1 =[]
#ims2 = []
def iE(e):
    return int((e + 2*N)/4)

def IntEnergy():
    exponent = 0.0      
    for T in arange (0.2, 8.2, 0.2 ):                 # Select lambda max
        Ener = - 2*N
        maxL = 0.0                                           # Initialize
        for i in range(0, N + 1):
            if S[i]!= 0 and (S[i] - Ener/T)>maxL:
                maxL = S[i] - Ener/T
                Ener = Ener + 4
        sumdeno = 0
        sumnume = 0
        Ener    = -2*N
        for i in range(0, N):
            if S[i] != 0:
                exponent = S[i] - Ener/T - maxL
            sumnume += Ener*exp(exponent)
            sumdeno += exp(exponent)
            Ener     = Ener +  4.0
        U = sumnume/sumdeno/N                    # internal energy U(T)/N
        #energ.plot(pos = (T, U) )
        x1list.append(T)
        y1list.append(U)
        

def WL():                                        # Wang - Landau sampling
    Hinf   = 1.0e10                         # initial values for Histogram
    Hsup   = 0.0
    tol    = 1.0e-3                       # tolerance, stops the algorithm
    ip     = zeros(L)
    im     = zeros(L)                             # BC R or down, L or up
    height = abs(Hsup - Hinf)/2.                   # Initialize histogram
    ave = (Hsup + Hinf)/2.                   # about average of histogram
    percent = height / ave  
    for i in range(0, L):
        for j in range(0, L):
            sp[i, j] = 1                # Initial spins
    for i in range(0, L):
         ip[i] = i + 1
         im[i] = i - 1                                 # Case plus, minus
    ip[L - 1] = 0
    im[0]     = L - 1                                           # Borders
    Eold = - 2*N                                      # Initialize energy
    for  j in range(0, N + 1):
        S[j] = 0             # Entropy initialized
    iter = 0
    fac  = 1
    while  fac > tol :
       
        i = int(N*random.random() )                  # Select random spin
        xg = i%L
        # Must be i//L, not i/L for Python 3:
        yg     =int(i//L)                         # Localize x, y, grid point
        Enew   = Eold + 2*(sp[int(ip[xg]),yg] + sp[int(im[xg]),yg] + sp[xg,int(ip[yg])]+ sp[xg, int(im[yg])] ) * sp[xg, int(yg)]              # Change energy
        deltaS = S[iE(Enew)]  -  S[iE(Eold)]
        if  deltaS <= 0 or random.random() < exp( - deltaS):
           Eold = Enew; 
           sp[xg, yg] *=  - 1                                 # Flip spin
        S[iE(Eold)]   += fac;                            # Change entropy
        if iter%10000 == 0:           # Check flatness every 10000 sweeps
           for j in range( 0, N + 1):
              if  j == 0 :
                  Hsup = 0
                  Hinf = 1e10                  # Initialize new histogram
              if  hist[j] == 0 :
                  continue       # Energies never visited
              if  hist[j] > Hsup:
                  Hsup = hist[j]
              if  hist[j] < Hinf:
                  Hinf = hist[j]
           height = Hsup - Hinf
           ave = Hsup + Hinf
           percent = 1.0* height/ave        # 1.0 to make it float number
           if percent < 0.3 :                           # Histogram flat?
                print(" iter ", iter, "   log(f) ", fac) 
                for j in range(0, N + 1):
                    prhist[j] = hist[j]                         # to plot
                    hist[j]   = 0                             # Save hist
                fac *= 0.5# Equivalent to log(sqrt(f))
                """
                for i in range(0, N+1):
                    x3list.append(2.0*i - N)
                    y3list.append(0.025*hist[i]-10)
                    im1 = plt.plot(x3list,y3list)
                    ims1.append(im1)
                """

        #x3list.clear()
        #y3list.clear()
        iter += 1
        hist[iE(Eold)]   += 1           # Change histogram, add 1, update
        

        if fac >= 0.5:                    # just show the first histogram
            # Speed up by using array calculations:
            #histo.x = 2.0*arange(0,N+1) - N
            #histo.y = 0.025*hist-10
            for i in range(0, N+1):
                x3list.append(2.0*i - N)
                y3list.append(0.025*hist[i]-10)
            # histってどこやねん
            #a=1
        #im1 = plt.plot(x3list,y3list)
        #ims1.append(im1)

        #x3list.clear()
        #y3list.clear()
        

            
deltaS = 0.0
print("wait because iter > 13 000 000")             # not always the same
WL()                                         # Call Wang Landau algorithm
deltaS = 0.0
for j in range(0, N + 1):
    #rate(150)
    order    = j*4  -  2*N
    deltaS   = S[j]  -  S[0] + log(2)
    if S[j] != 0 :
        #entrp.plot(pos = (1.*order/N, deltaS))   # plot entropy
        x2list.append(1.0*order/N)
        y2list.append(deltaS)

IntEnergy()
print("Done")


fig1 = plt.figure(figsize=(5 , 2.5))
plt.title('E vs T')
plt.xlabel('T')
plt.ylabel('U(T)/N')
plt.plot(x1list,y1list)


fig2 = plt.figure(figsize =(5,2.5))
plt.title('Density of States')
plt.xlabel('E/N')
plt.ylabel('log g(E)')
plt.plot(x2list,y2list)
"""
fig3 = plt.figure(figsize =(5,3))
plt.title('1st histogram: H(E) vs. E/N, corresponds to log(f) = 1')
ani1 = animation.ArtistAnimation(fig1,ims1,interval=100 ,repeat_delay = 1000)
"""
fig3 = plt.figure(figsize =(5,3))
plt.title('1st histogram: H(E) vs. E/N, corresponds to log(f) = 1')
plt.plot(x3list,y3list)

plt.show()

#hist はanimation で表示させるのだろうか
#hist overflow してしまう

""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# IsingViz.py: Ising model

#from visual import *
import random
#from visual.graph import *
import matplotlib.pyplot as plt
from numpy import *
import matplotlib.animation as animation

# Display for the arrows

"""
scene = display(x=0,y=0,width=700,height=200, range=40,title='Spins')
engraph = gdisplay(y=200,width=700,height=300, title='E of Spin System',\
        xtitle='iteration', ytitle='E',xmax=500, xmin=0, ymax=5, ymin=-5)
enplot = gcurve(color=color.yellow)                  
"""

N     = 30                                               
B     = 1.0                                                
mu    = 0.33                                             # g mu
J     = 0.20                                              
k     = 1.0                                            # Boltmann
T     = 100.0                                                 
state = zeros((N))                            # spins up(1), down (0)
S     = zeros((N) ,float)                   
test  = state                                               
random.seed()                                        # Seed generator

xlist = []
ylist = []
x1list =[]
y1list =[]
x2list = []
y2list = []
colorlist = []
ims1 =[]
ims2 = []

def energy (S) :                                  
    FirstTerm = 0.
    SecondTerm = 0.                                          
    for  i in range(0,N-2):
        FirstTerm += S[i]*S[i + 1]
    FirstTerm *= -J 
    for i in range(0,N-1):
        SecondTerm += S[i]
    SecondTerm *= -B*mu; 
    return (FirstTerm + SecondTerm); 
		
ES = energy(state)                                   

def spstate(state, time):                                        # Plots spins
    """
    for obj in scene.objects:
        obj.visible=0         # Erase old arrows
    """
    #x1list.clear
    #y1list.clear
    j=0    
    for i in range(-N,N,2):               
        if state[j]==-1:
            ypos = 5                          # Spin down
        else:
            ypos = 0
        if  5*state[j]<0:
            #arrowcol = 'white'    # White arrow if down
            x1list.append(i)
            y1list.append(time)
        else:
            x2list.append(i)
            y2list.append(time)
            #arrowcol = 'black'
        #arrow(pos=(i,ypos,0),axis=(0,5*state[j],0),color=arrowcol)
            
        #x1list.append(state[j])
        #y1list.append(i)
        #colorlist.append(arrowcol)
        #plt.pause(0.01)
        #plt.plot(i,ypos,color = 'arrowcol')
        j +=1
        
for  i in range(0 ,N):
    state[i] = -1          # Initial spins all down

"""
for obj in scene.objects:
    obj.visible=0    # Erase old arrows
"""
"""
x1list.clear()
y1list.clear()
x2list.clear()
y2list.clear()
"""
time = 0
spstate(state,time)                       
ES = energy(state)                   
                                     
for  j in range (1,500):             
      #rate(3)
      plt.pause(0.01)
      test = state                   
      r = int(N*random.random());  # Flip spin randomly
      test[r] *= -1                  
      ET = energy(test)              
      p = math.exp((ES-ET)/(k*T))   #  Boltzmann test
      #enplot.plot(pos=(j,ES))       # Adds segment to curve
      xlist.append(j)
      ylist.append(ES)
      time = j
      if p >= random.random():       
           state = test
           spstate(state,time)
           im1 = plt.plot(y1list,x1list,'o',color ='white')
           im2 = plt.plot(y2list,x2list,'o',color ='blue')
           ims1.append(im1)
           ims2.append(im2)
           """
           x1list.clear()
           y1list.clear()
           x2list.clear()
           y2list.clear()
           """
           ES = ET
           

fig0 = plt.figure(figsize=(7,3))
plt.title('E of Spin System')
plt.xlabel('iteration')
plt.ylabel('E')
plt.plot(xlist,ylist,'yellow')

"""

ax =fig.add_subplot(111)
ax.grid()
plt.title('Spins')
plt.plot(x1list,y1list,color = colorlist)
"""
fig1 = plt.figure(figsize=(7,2))
plt.xlim(-N,N)
plt,ylim(0,500)
ani1 =  animation.ArtistAnimation(fig1,ims1,interval=1 ,repeat_delay = 1000)
ani2 =  animation.ArtistAnimation(fig1,ims2,interval=1 ,repeat_delay = 1000)

plt.show()  

#計算時間が長すぎて二つのグラフが同時に表示されない
#xlim , ylim で固定してくれない

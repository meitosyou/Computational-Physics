"""
レナード-ジョーンズ原子の2次元分子動力学シミュレーション

Sept. 2017
"""

%matplotlib nbagg  #jupyter上でmatplotlibのアニメーションを再現する

import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure(figsize = (8, 6))
ims = []


lat_x = 1.291 # 格子定数: x
lat_y = 1.291
Lx = 5 # 格子点: x
Ly = 5 
N_atom = Lx*Ly
m=1 # 質量

delta_t = 0.002 # MDステップの間隔

T_initial = 50  # initial temperature [K]
T_initial = T_initial /119 # convert to natural unit


Max_step = 1000  #MD ステップ数

x = np.zeros([N_atom],float)
y = np.zeros([N_atom],float)

vx = np.zeros([N_atom],float)
vy = np.zeros([N_atom],float)

fx = np.zeros([N_atom,2],float)# Q: What is this "2"?
fy = np.zeros([N_atom,2],float)   


# step毎の物理量の格納
T_lis = []
P_lis =  []
KE_lis =[]
PE_lis =[]
Eot_lis =[]
Tav_lis = []
Pav_lis =  []
KEav_lis =[]
PEav_lis =[]
Eotav_lis =[]
##

density = N_atom/(Lx*Ly*lat_x*lat_y) # 数密度: 2次元

print ("number density = ", density)
def twelveran():
    s = 0
    for i in range(1,13):
        s += random.random()
    return s/12.0 - 0.5


def Maxwell_velocity2D(TT): # マクスウェルの速度分布: ボックス-ミュラー法: self 
    for i in range(N_atom):
        R1=random.random()
        R2=random.random()
        R3=random.random()
        R4=random.random()
        vx[i] = (np.sqrt(-2* (TT/m)*np.log(R1)))*np.cos(2*np.pi*R2)
        vy[i] = (np.sqrt(-2* (TT/m)*np.log(R3)))*np.cos(2*np.pi*R4)

def initialposMaxwellvel():
    i=-1
    for ix in range(Lx):
        for iy in range(Ly):
            i += 1
            x[i] = lat_x*ix
            y[i] = lat_y*iy

    Maxwell_velocity2D(T_initial)





def sign(a,b):
    if b >= 0:
        return abs(a)
    else:
        return -abs(a)

def Forces(t,w,PE,PEorW):
    rcut = 4 # 力のカットオフ半径
    PE = 0

    r2cut = rcut**2


    fx[:,t] = 0
    fy[:,t] = 0
    for i in range(N_atom-1):
        for j in range(i+1, N_atom):
            dx = x[i] - x[j]
            dy = y[i] - y[j]

            # 近接イメージ(鏡像)相互作用
            if (abs(dx) > 0.5*lat_x*Lx):
                dx = dx - sign(lat_x*Lx,dx)
            if (abs(dy) > 0.5*lat_y*Ly):
                dy = dy-sign(lat_y*Ly,dy)
            r2 = dx**2+dy**2

            if (r2 < r2cut):
                if r2 == 0 :
                    r2 = 0.0001
                invr2 = 1/r2

                wij = 48*(invr2**3-0.5)*(invr2**3)
                fijx = wij*invr2*dx
                fijy = wij*invr2*dy

                fx[i,t] += fijx
                fy[i,t] += fijy
                fx[j,t] -= fijx
                fy[j,t] -= fijy

                PE += 4*(invr2**3)*((invr2**3)-1)
                w += wij
    if (PEorW == 1) :
        return PE
    else :
        return w

# メイン: 時間発展
def time_evolution():

    avT = 0
    avP = 0
    Pavg = 0
    avKE=0
    avPE=0

    t1 = 0
    PE = 0.0

    # 初期化
    KE = 0
    w = 0

    initialposMaxwellvel()  # 初期状態の構築

    KE = (np.sum(vx**2)+np.sum(vy**2))/2
    T = KE/N_atom
    P = density*(2*KE+1.5*w)/(3*N_atom) # 圧力の計算(2次元系)

    PE = Forces(t1, w, PE, 1)
    time = 1   
    n_step=0

    # 値の保存
    T_lis.append(T*119) # K 単位
    P_lis.append(P*2.382*1e-8)  # Pa 単位
    KE_lis.append(KE/N_atom)
    PE_lis.append(PE/N_atom)
    dumEtot = KE+PE
    Eot_lis.append( dumEtot /N_atom)


    while n_step < Max_step:  #どうやらwhileが絡むとループ抜けないから表示のところまでプログラムがいかないらしい
        if n_step % 50 ==0: 
            print ("step=",n_step)
            #print("T=",T*119,"K/N = ",KE/N_atom," Pot/N = ",PE/N_atom," Etot/N = ",(KE+PE)/N_atom, " P=",P)

        #print("x[0] =",x[0] )
       # ax.set_title("t ="  + str("{0:.1f}".format(n_step*delta_t)))

        if n_step % 5 ==0:
            im=plt.scatter(x, y, s=120, c="red", alpha=0.9, linewidths="1.5",edgecolors="black")
            ims.append([im])      

        n_step += 1



        for i in range(N_atom):   
            PE = Forces(t1, w, PE, 1)    
            # 速度ベルレー法による更新
            x[i] +=delta_t*(vx[i]+delta_t*fx[i,t1]/2)
            y[i] +=delta_t*(vy[i]+delta_t*fy[i,t1]/2)

            if x[i] <= 0: 
                x[i] += lat_x*Lx
            if x[i] >= lat_x*Lx:
                x[i] -= lat_x*Lx
            if y[i] <= 0:
                y[i]  += lat_y*Ly
            if y[i] >= lat_y*Ly:
                y[i] -= lat_y*Ly



        PE = 0.
        t2=1
        PE = Forces(t2, w, PE, 1)

        KE = 0.
        w = 0.



            #for i in range(N_atom):
        # 速度ベルレー法による更新
        vx[:] += delta_t*(fx[:,t1]+fx[:,t2])/2
        vy[:] += delta_t*(fy[:,t1]+fy[:,t2])/2

        KE =(np.sum(vx**2)+np.sum(vy**2))/2




        w = Forces(t2, w, PE, 2)
        T = KE/N_atom

        #        P = density*(KE + w)
        P = density*(2*KE+1.5*w)/(3*N_atom) # 圧力の計算




        #平均値
        avT += T
        avP += P
        avKE += KE
        avPE += PE
        time +=1
        t = time
        if (t == 0):
             t = 1

        # 時間平均
        Pavg =avP/t
        eKavg = avKE/t
        ePavg = avPE/t
        Tavg = avT/t

        T_lis.append(T*119) # K 単位
        P_lis.append(P*2.382*1e-8)  # Pa 単位
        KE_lis.append(KE/N_atom)
        PE_lis.append(PE/N_atom)
        dumEtot = KE+PE
        Eot_lis.append( dumEtot /N_atom)

        Tav_lis.append(Tavg*119 )# K 単位
        Pav_lis.append(Pavg*2.382*1e-8) 
        KEav_lis.append(eKavg/N_atom)
        PEav_lis.append(ePavg/N_atom)





##

time_evolution() #メイン

# プロット+動画の保存
plt.axis([0,lat_x*Lx,0,lat_y*Ly])
ani = animation.ArtistAnimation(fig, ims, interval =1)
plt.show() 
ani.save("output.gif", writer="imagemagick")

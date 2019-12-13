import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import winsound

# メイン実行部
# 試行回数nの初期化
lambda1 = 0.005
max = 80
time_max = 500
seed = 68111
number = nloop = max
fig = plt.figure()
plt.title('Spontaneous Decay')
plt.xlabel('Time')
plt.ylabel('Number')

ims = []
N = number
t = 0.0
# グラフ描画の準備
tlist = [t]  # x座標
Nlist = [N]  # y座標

# ランダムウォーク
for time in range(0, time_max +1):
    tlist.append(time)
    Nlist.append(number)
    im = plt.plot(tlist, Nlist, marker='o', color = 'yellow')
    ims.append(im)
    for atom in np.arange(1 , number+1):
        decay = random.random()
        if (decay < lambda1):
            nloop = nloop -1
            winsound.Beep(600 ,100)
    number = nloop

# グラフの表示
plt.show()
ani = animation.ArtistAnimation(fig,ims,interval=30)


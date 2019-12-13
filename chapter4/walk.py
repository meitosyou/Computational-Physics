
# モジュールのインポート
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# メイン実行部
# 試行回数nの初期化
n = 20
fig = plt.figure()
plt.title('Random Walk')
plt.xlabel('x')
plt.ylabel('y')

ims = []
x = 0.0
y = 0.0
# グラフ描画の準備
xlist = [x]  # x座標
ylist = [y]  # y座標
# ランダムウォーク
for i in range(n):
    xlist.append(x)
    ylist.append(y)
    x += (random.random() -0.5 )*2
    y += (random.random() -0.5 )*2
    im = plt.plot(xlist, ylist, marker='o', color = 'yellow')
    ims.append(im)

# グラフの表示
ani = animation.ArtistAnimation(fig,ims,interval=100 ,repeat_delay = 500)
plt.show()

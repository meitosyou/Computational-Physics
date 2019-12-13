import math

import numpy as np
from matplotlib import pyplot as plt


def main():
    # 描画領域
    fig = plt.figure(figsize=(10, 6))
    plt.title('pyplot 2D plot')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    fig.patch.set_facecolor('white')  # 図全体の背景色
    ax = fig.add_subplot(111)  # Axes
    ax.patch.set_facecolor('green')  # subplotの背景色

    # foreground
    #background
    #二つのグラフの分離

    # 描画するデータ
    x1 = np.arange(0 , 8.1 , 0.1)
    y1 = [5*np.cos(2*j) *np.exp(-0.4*j) for j in x1]

    
    x2 = np.arange(-5, +5, 0.1)
    y2 = [math.cos(i) for i in x2]

    # グラフを描画する
    plt.plot(x1, y1, 'white')
    plt.plot(x2, y2, 'black') 

    # グラフを表示する
    plt.show()


if __name__ == '__main__':
    main()

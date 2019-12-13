from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plot
import numpy as np

def generate(X, Y, phi):
    return np.sin(X + 3 * phi) + np.cos(Y + 5 * phi)

fig = plot.figure()
ax = fig.add_subplot(111, projection='3d')

xs = np.linspace(-np.pi, np.pi, 100)
ys = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(xs, ys)

Z = generate(X, Y, 0.0)
wf = ax.plot_wireframe(X, Y, Z)

for phi in np.linspace(0, 2 * np.pi, 100):

    old_wf = wf

    Z = generate(X, Y, phi)
    wf = ax.plot_wireframe(X, Y, Z)

    ax.collections.remove(old_wf)

    plot.pause(0.01)

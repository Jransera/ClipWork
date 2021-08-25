from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors
import matplotlib.pyplot as plt
import numpy as np
import re
import random


#open the file and split the data by line
with open('Data.txt') as f:
    lines = f.readlines()
    xz = []
    yz=  []
    #xz is the image file, we must parse the title to get these values
    for line in lines:
        xz.append(line.split(',')[0])
        yz.append(line.split(',')[1])

    parseChar = '()\n'
    zs = []
    for y in yz:
        zs.append(float(y[:-2]))




# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
xs = []
ys = []

for l in xz:
    parsed = re.split('[aet]',l)

    parsed[1] = parsed[1][:-1]
    parsed[2] = parsed[2][:-1]

    xs.append(float(parsed[1]))

    ys.append(float(parsed[2]))

nxs = np.array(xs)
nys = np.array(ys)
nzs = np.array(zs)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u, v = np.meshgrid(nxs, nys)

strength = nzs
norm=colors.Normalize(vmin = np.min(strength),
                      vmax = np.max(strength), clip = False)

x = 10 * np.sin(u) * np.cos(v)
y = 10 * np.sin(u) * np.sin(v)
z = 10 * np.cos(u)

ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False,
                       facecolors=cm.coolwarm(norm(strength)))

plt.show()

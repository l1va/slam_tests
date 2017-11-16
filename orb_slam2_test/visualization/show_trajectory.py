from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

ax = Axes3D(pyplot.figure())
ax1 = Axes3D(pyplot.figure())
ax2 = Axes3D(pyplot.figure())
ax3 = Axes3D(pyplot.figure())

with open("KeyFrameTrajectory.txt") as f:
    frames = f.readlines()

xs, ys, zs = [], [], []
for frame in frames:
    fr = frame.split()
    xs.append(float(fr[1]))  # timestamp tx ty tz qx qy qz qw
    ys.append(float(fr[2]))
    zs.append(float(fr[3]))


def scatter(ax, title, xs, ys, zs):
    ax.scatter(xs, ys, zs)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.text2D(0.05, 0.95, title, transform=ax.transAxes)
    ax.text(xs[0], ys[0], zs[0], "start", color='red')


scatter(ax, "All laps", xs, ys, zs)
p1 = 185
p2 = 307
scatter(ax1, "First lap", xs[:p1], ys[:p1], zs[:p1])
scatter(ax2, "Second lap", xs[p1:p2], ys[p1:p2], zs[p1:p2])
scatter(ax3, "Third lap", xs[p2:], ys[p2:], zs[p2:])

pyplot.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import My_lib as ml


def fun(x, y, z):
    return ((x**2)/(1**2))+((y**2)/(1.5**2))+((z**2)/(2**2))


analyt_val = 12.56637
N = 10000
Fn, X1, Y1, Z1, frac_err = ml.monte_carlo_volume(
    -1, 1, -1.5, 1.5, -2, 2, fun, N, analyt_val)

print("\nVolume = ", Fn)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X1, Y1, Z1)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()


'''
Output

Volume =  12.530399999999998
'''

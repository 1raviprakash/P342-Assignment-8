import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import My_lib as M_L


def fun(x, y, z):
    return ((x**2)/(1**2))+((y**2)/(1.5**2))+((z**2)/(2**2))


Analytical_Val = 12.56637
N = 10000
Fn, X1, Y1, Z1, frac_err = M_L.Monte_Carlo_Vol(
    -1, 1, -1.5, 1.5, -2, 2, fun, N, Analytical_Val)
print("\nVolume = ", Fn)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X1, Y1, Z1)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()


'''
Output

Volume =  12.463199999999999
'''

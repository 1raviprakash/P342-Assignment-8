import My_lib as ml
import matplotlib.pyplot as plt
import math

figure, axes = plt.subplots(nrows=2, ncols=3)


RMS = []
steps = []

M = 100
N = 250
add = 200
print("\n\nFor Steps = 250; No. of walks = 5 : ")

X1, Y1, r_rms1, avg_x1, avg_y1, rad_dis1 = ml.random_walk(M, N)

print("Rrms = ", r_rms1)
print("rootN = ", math.sqrt(N))
print("Average X = ", avg_x1)
print("Average Y = ", avg_y1)
print("Radial distance R = ", rad_dis1)

RMS.append(r_rms1)
steps.append(math.sqrt(N))
for i in range(5):
    axes[0, 0].set_xlabel('X')
    axes[0, 0].set_ylabel('Y')
    axes[0, 0].grid(True)
    axes[0, 0].set_title("For steps = 250; walks = 5")
    axes[0, 0].plot(X1[i], Y1[i])


N = N + add
print("\n\nFor Steps =", N, "; No. of walks =", M, ": ")
X2, Y2, r_rms2, avg_x2, avg_y2, rad_dis2 = ml.random_walk(M, N)

print("Rrms = ", r_rms2)
print("rootN = ", math.sqrt(N))
print("Average X = ", avg_x2)
print("Average Y = ", avg_y2)
print("Radial distance R = ", rad_dis2)
RMS.append(r_rms2)
steps.append(math.sqrt(N))

for i in range(5):
    axes[0, 1].set_xlabel('X')
    axes[0, 1].set_ylabel('Y')
    axes[0, 1].grid(True)
    axes[0, 1].set_title("For steps = 450; walks = 5")
    axes[0, 1].plot(X2[i], Y2[i])


N = N + add
print("\n\nFor Steps =", N, "; No. of walks =", M, ": ")
X3, Y3, r_rms3, avg_x3, avg_y3, rad_dis3 = ml.random_walk(M, N)

print("Rrms = ", r_rms3)
print("rootN = ", math.sqrt(N))
print("Average X = ", avg_x3)
print("Average Y = ", avg_y3)
print("Radial distance R = ", rad_dis3)

RMS.append(r_rms3)
steps.append(math.sqrt(N))

for i in range(5):
    axes[0, 2].set_xlabel('X')
    axes[0, 2].set_ylabel('Y')
    axes[0, 2].grid(True)
    axes[0, 2].set_title("For steps = 650; walks = 5")
    axes[0, 2].plot(X3[i], Y3[i])


N = N + add
print("\n\nFor Steps =", N, "; No. of walks =", M, ": ")
X4, Y4, r_rms4, avg_x4, avg_y4, rad_dis4 = ml.random_walk(M, N)

print("Rrms = ", r_rms4)
print("rootN = ", math.sqrt(N))
print("Average X = ", avg_x4)
print("Average Y = ", avg_y4)
print("Radial distance R = ", rad_dis4)

RMS.append(r_rms4)
steps.append(math.sqrt(N))

for i in range(5):
    axes[1, 0].set_xlabel('X')
    axes[1, 0].set_ylabel('Y')
    axes[1, 0].grid(True)
    axes[1, 0].set_title("For steps = 850; walks = 5")
    axes[1, 0].plot(X4[i], Y4[i])

N = N + add
print("\n\nFor Steps =", N, "; No. of walks =", M, ": ")

X5, Y5, r_rms5, avg_x5, avg_y5, rad_dis5 = ml.random_walk(M, N)

print("Rrms = ", r_rms5)
print("rootN = ", math.sqrt(N))
print("Average X = ", avg_x5)
print("Average Y = ", avg_y5)
print("Radial distance R = ", rad_dis5)
RMS.append(r_rms5)
steps.append(math.sqrt(N))


for i in range(5):
    axes[1, 1].set_xlabel('X')
    axes[1, 1].set_ylabel('Y')
    axes[1, 1].grid(True)
    axes[1, 1].set_title("For steps = 1050; walks = 5")
    axes[1, 1].plot(X5[i], Y5[i])
# figure.tight_layout()
plt.figure()
plt.title("Rrms vs root of N plot for Steps(N) = 250, 450, 650, 850, 1050.")
plt.ylabel('Rrms')
plt.xlabel('Root of N')
plt.plot(steps, RMS)

plt.grid(True)
plt.show()


'''
Output


For Steps = 250; No. of walks = 5 : 
Rrms =  16.137042365767844
rootN =  15.811388300841896
Average X =  -1.371902780508386
Average Y =  0.24597364371600558
Radial distance R =  1.3937791333527596


For Steps = 450 ; No. of walks = 100 : 
Rrms =  21.55064886579121
rootN =  21.213203435596427
Average X =  1.7339482217304585
Average Y =  -0.3878280633285131
Radial distance R =  1.7767912208099645


For Steps = 650 ; No. of walks = 100 : 
Rrms =  23.040076861828823
rootN =  25.495097567963924
Average X =  -0.09740814337446622
Average Y =  3.1320380194412145
Radial distance R =  3.133552377354


For Steps = 850 ; No. of walks = 100 : 
Rrms =  28.854642398812068
rootN =  29.154759474226502
Average X =  0.31444081596456014
Average Y =  -2.2193900178625983
Radial distance R =  2.241554165781546


For Steps = 1050 ; No. of walks = 100 : 
Rrms =  30.85079429810423
rootN =  32.4037034920393
Average X =  0.18129868314510747
Average Y =  -0.9391849114370308
Radial distance R =  0.9565236590807011

'''

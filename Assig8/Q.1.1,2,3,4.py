import My_lib as M_L
import matplotlib.pyplot as plt
import math


figure, axes = plt.subplots(nrows=2, ncols=3)
RMS = []
steps = []

M = 100
N = 250
add = 250
print("\n\nSteps no. = 250; No. of walks = 5 : ")

X1, Y1, R_RMS1, Avg_X1, Avg_Y1, Radial_dis1 = M_L.Ran_Walk(M, N)

print("Rrms = ", R_RMS1)
print("rootN = ", math.sqrt(N))
print("Average X = ", Avg_X1)
print("Average Y = ", Avg_Y1)
print("Radial distance R = ", Radial_dis1)

RMS.append(R_RMS1)
steps.append(math.sqrt(N))
for i in range(5):
    axes[0, 0].set_xlabel('X')
    axes[0, 0].set_ylabel('Y')
    axes[0, 0].grid(True)
    axes[0, 0].set_title("For no of steps = 250; walks = 5")
    axes[0, 0].plot(X1[i], Y1[i])


N = N + add
print("\n\nSteps no. =", N, "; No. of walks =", M, ": ")
X2, Y2, R_RMS2, avg_x2, avg_y2, Radial_dis2 = M_L.Ran_Walk(M, N)

print("Rrms = ", R_RMS2)
print("rootN = ", math.sqrt(N))
print("Average X = ", avg_x2)
print("Average Y = ", avg_y2)
print("Radial distance R = ", Radial_dis2)
RMS.append(R_RMS2)
steps.append(math.sqrt(N))

for i in range(5):
    axes[0, 1].set_xlabel('X')
    axes[0, 1].set_ylabel('Y')
    axes[0, 1].grid(True)
    axes[0, 1].set_title("Steps no. = 500; walks = 5")
    axes[0, 1].plot(X2[i], Y2[i])


N = N + add
print("\n\nSteps no. =", N, "; No. of walks =", M, ": ")
X3, Y3, R_RMS3, avg_x3, avg_y3, Radial_dis3 = M_L.Ran_Walk(M, N)

print("Rrms = ", R_RMS3)
print("rootN = ", math.sqrt(N))
print("Average X = ", avg_x3)
print("Average Y = ", avg_y3)
print("Radial distance R = ", Radial_dis3)

RMS.append(R_RMS3)
steps.append(math.sqrt(N))

for i in range(5):
    axes[0, 2].set_xlabel('X')
    axes[0, 2].set_ylabel('Y')
    axes[0, 2].grid(True)
    axes[0, 2].set_title("Steps no. = 750; walks = 5")
    axes[0, 2].plot(X3[i], Y3[i])


N = N + add
print("\n\nSteps no. =", N, "; No. of walks =", M, ": ")
X4, Y4, R_RMS4, avg_x4, avg_y4, Radial_dis4 = M_L.Ran_Walk(M, N)

print("Rrms = ", R_RMS4)
print("rootN = ", math.sqrt(N))
print("Average X = ", avg_x4)
print("Average Y = ", avg_y4)
print("Radial distance R = ", Radial_dis4)

RMS.append(R_RMS4)
steps.append(math.sqrt(N))

for i in range(5):
    axes[1, 0].set_xlabel('X')
    axes[1, 0].set_ylabel('Y')
    axes[1, 0].grid(True)
    axes[1, 0].set_title("Steps no. = 1000; walks = 5")
    axes[1, 0].plot(X4[i], Y4[i])

N = N + add
print("\n\nSteps no. =", N, "; No. of walks =", M, ": ")

X5, Y5, R_RMS5, avg_x5, avg_y5, Radial_dis5 = M_L.Ran_Walk(M, N)

print("Rrms = ", R_RMS5)
print("rootN = ", math.sqrt(N))
print("Average X = ", avg_x5)
print("Average Y = ", avg_y5)
print("Radial distance R = ", Radial_dis5)
RMS.append(R_RMS5)
steps.append(math.sqrt(N))


for i in range(5):
    axes[1, 1].set_xlabel('X')
    axes[1, 1].set_ylabel('Y')
    axes[1, 1].grid(True)
    axes[1, 1].set_title("Steps no. = 1250; walks = 5")
    axes[1, 1].plot(X5[i], Y5[i])
# figure.tight_layout()
plt.figure()
plt.title("Rrms vs root of N plot Steps no.(N) = 250, 500, 750, 1000, 1250.")
plt.ylabel('Rrms')
plt.xlabel('Root of N')
plt.plot(steps, RMS)

plt.grid(True)
plt.show()


'''
Output


Steps no. = 250; No. of walks = 5 : 
Rrms =  16.22837432143171
rootN =  15.811388300841896
Average X =  0.7051874795084889
Average Y =  0.015954272176341724
Radial distance R =  0.7053679323985549


Steps no. = 500 ; No. of walks = 100 : 
Rrms =  22.143057625317333
rootN =  22.360679774997898
Average X =  -1.7708982170339356
Average Y =  -0.15034097363701848
Radial distance R =  1.7772683825039195


Steps no. = 750 ; No. of walks = 100 : 
Rrms =  28.01606103492616
rootN =  27.386127875258307
Average X =  -1.4148439010530565
Average Y =  -0.04797944447068421
Radial distance R =  1.415657194181821


Steps no. = 1000 ; No. of walks = 100 : 
Rrms =  32.153361267166886
rootN =  31.622776601683793
Average X =  0.05196840123449368
Average Y =  -0.7062356521565364
Radial distance R =  0.708145120087569


Steps no. = 1250 ; No. of walks = 100 : 
Rrms =  32.670590388115954
rootN =  35.35533905932738
Average X =  -3.941301167721115
Average Y =  2.3262914470749685
Radial distance R =  4.576623951278275
'''

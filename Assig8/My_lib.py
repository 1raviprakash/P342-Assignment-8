# Library used in making this library
import math
import random
import time
import matplotlib.pyplot as plt

# 1. Reading a Matrix from a file


def read_Matrix(fil, A):
    file = open(fil, 'r')
    for line in file:
        ns = line.split()
        no = [float(n) for n in ns]
        A.append(no)
    file.close()


# 2. To print the Matrix
def write_Matrix(x):
    for r in range(len(x)):
        print(x[r])


# 3. Factorial Method
def factorial(num):
    fact = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            fact = fact * i
        return fact


# 4. Function for partial pivoting the Augmented Matrix / Only Matrix
def partial_pivot(a, b):
    n = len(a)
    counter = 0
    for r in range(0, n):
        if abs(a[r][r]) == 0:
            for r1 in range(r+1, n):
                if abs(a[r1][r]) > abs(a[r][r]):
                    counter = counter + 1
                    for x in range(0, n):
                        d1 = a[r][x]
                        a[r][x] = a[r1][x]
                        a[r1][x] = d1
                    if(b != 0):
                        d1 = b[r]
                        b[r] = b[r1]
                        b[r1] = d1
    return counter


# 5. Multiplication of Matrices
def matrix_Multiplication(a, b):
    m = len(b[0])
    l = len(b)
    n = len(a)
    p2 = [[0 for y in range(m)] for x in range(n)]
    for x in range(n):
        for i in range(m):
            for y in range(l):
                p2[x][i] = p2[x][i] + (a[x][y] * b[y][i])
    return p2


# 6. Gauss-Jordan Method
def gauss_Jordan(a, b):
    n = len(a)
    bn = len(b[0])
    for r in range(0, n):
        partial_pivot(a, b)
        pivot = a[r][r]
        for c in range(r, n):
            a[r][c] = a[r][c]/pivot
        for c in range(0, bn):
            b[r][c] = b[r][c]/pivot
        for r1 in range(0, n):
            if r1 == r or a[r1][r] == 0:
                continue
            else:
                factor = a[r1][r]
                for c in range(r, n):
                    a[r1][c] = a[r1][c] - factor*a[r][c]
                for c in range(0, bn):
                    b[r1][c] = b[r1][c] - factor*b[r][c]


# 7. Forward- Backward Substitution
def forwardbackward_Substitution(a, b):
    m = len(b[0])
    n = len(a)
    # forward substitution
    y = [[0 for y in range(m)] for x in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(i):
                s = s + a[i][k] * y[k][j]
            y[i][j] = b[i][j] - s
    # backward substitution
    x = [[0 for y in range(m)] for x in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m):
            s = 0
            for k in range(i + 1, n):
                s = s + a[i][k] * x[k][j]
            x[i][j] = (y[i][j] - s) / a[i][i]

    return x


# 8. L-U decomposition
def lu_Decomposition(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            s = 0
            if(i <= j):
                for k in range(i):
                    s = s + (a[i][k] * a[k][j])
                a[i][j] = a[i][j] - s
            else:
                for k in range(j):
                    s = s + (a[i][k] * a[k][j])
                a[i][j] = (a[i][j] - s) / a[j][j]


# 9. Finding determinant of Upper Triangular Matrix
def uppertriangular_Determinant(a):
    n = len(a)
    p = 1
    for i in range(n-2):
        p = p * a[i][i]
    p = p * (a[n-2][n-2] * a[n-1][n-1])
    return p


# 10. Bracketing the root
def bracket_Root(f, a):
    fa = f(a[0])
    fb = f(a[1])
    beta = 0.7
    for i in range(12):
        if ((fa * fb) < 0):
            return True
        if((fa * fb) > 0):
            if(abs(fa) < abs(fb)):
                a[0] = a[0] - beta * (a[1] - a[0])
            elif(abs(fa) > abs(fb)):
                a[1] = a[1] + beta * (a[1] - a[0])
        i = i+1
    if ((fa * fb) < 0):
        return True
    else:
        return False


# 11. Bisection method for root, where f is function and a are guess values
def bisection_Root(f, a):
    epsilon = pow(10, -6)
    if (bracket_Root(f, a)):
        for i in range(200):
            c = (a[0] + a[1]) / 2
            if ((f(a[0]) * f(c)) < 0):
                a[1] = c
            elif ((f(a[0]) * f(c)) > 0):
                a[0] = c
            elif((f(a[0]) * f(c)) == 0):
                if(abs(f(c)) == 0):
                    print("The root is", c)
                    return True
                elif(abs(f(a[0])) == 0):
                    print("The root is", a[0])
                    return True
            j = open("q1bbisectionfile.txt", 'a')
            j.write("%i         %5.21f\n" % (i+1, abs(a[1]-a[0])))
            j.close()
            if (abs(a[1] - a[0]) < epsilon):
                return True
    else:
        print("Very bad guess for bracketing")
        return False


# 12. False Position method for root, where f is function and a are guess values
def regularfalsi_Root(f, a):
    epsilon = pow(10, -6)
    z = 0
    if (bracket_Root(f, a)):
        for i in range(200):
            if(i != 0):
                z = c
            c = a[1] - (((a[1] - a[0]) * f(a[1])) / (f(a[1]) - f(a[0])))
            if ((f(a[0]) * f(c)) < 0):
                a[1] = c
            elif ((f(a[0]) * f(c)) > 0):
                a[0] = c
            elif((f(a[0]) * f(c)) == 0):
                if(abs(f(c)) == 0):
                    print("The root is", c)
                    return True
                elif(abs(f(a[0])) == 0):
                    print("The root is", a[0])
                    return True
            j = open("q1bregularfalsifile.txt", 'a')
            j.write("%i         %5.21f\n" % (i+1, abs(z - c)))
            j.close()
            if(i != 0):
                if (abs(z - c) < epsilon):
                    a[1] = c
                    return True
    else:
        print("Very bad guess for bracketing")
        return False


# 13. Finding first derivative
def first_Derivative(f, x):
    h = math.pow(10, -4)
    return ((f(x + h) - f(x - h)) / (2 * h))


# 14. Newton Raphson
def newtonraphson_Root(f, x):
    x1 = x
    epsilon = pow(10, -6)
    for i in range(200):
        n = f(x1)
        m = first_Derivative(f, x1)
        x1 = x1 - (n / m)
        j = open("q1bnewtonraphsonfile.txt", 'a')
        j.write("%i         %5.21f\n" % (i + 1, abs(x1 - x)))
        j.close()
        if (abs(x1 - x) < epsilon):
            return x1
        x = x1


# 15. Finding the First Derivative of polynomial, where p is polynomial method, c is coefficient array, i is the step of synthetic division, x is the value
def polynomialfirst_Derivative(p, c, i, x):
    h = math.pow(10, -6)
    return ((p(c, i, (x+h)) - p(c, i, (x-h))) / (2 * h))


# 16. Finding second derivative of polynomial, where p is polynomial method, c is coefficient array, i is the step of synthetic division, x is the value
def polynomialsecond_Derivative(p, c, i, x):
    h = math.pow(10, -6)
    m = polynomialfirst_Derivative(p, c, i, x + h)
    n = polynomialfirst_Derivative(p, c, i, x - h)
    return ((m - n) / (2 * h))


# 17. Synthetic Division Method for Deflation of Polynomials, where p is polynomial method, c is coefficient array, a0 is the guess value, r is solution array
def synthetic_Division(p, c, a0, r):
    for i in range(len(c) - 2):
        x1 = laguerre_Method(p, c, i, a0)
        for j in range(3 - i):
            c[j+1] = c[j+1] + (x1 * c[j])
        c[len(c) - 1 - i] = 0
        r.append(x1)


# 18. Laguerre Method for roots of polynomial, where p is polynomial method, c is coefficient array, i is the step of synthetic division, a0 is the guess value
def laguerre_Method(p, c, i, a0):
    e = len(c) - 1
    epsilon = math.pow(10, -4)
    if(p(c, i, a0) == 0):
        return a0
    else:
        for j in range(100):
            g = (polynomialfirst_Derivative(p, c, i, a0)) / p(c, i, a0)
            h = (math.pow(g, 2)) - \
                ((polynomialsecond_Derivative(p, c, i, a0)) / p(c, i, a0))
            d1 = (g + math.sqrt(abs((e-i-1)*(((e-i) * h) - math.pow(g, 2)))))
            d2 = (g - math.sqrt(abs((e-i-1)*(((e-i) * h) - math.pow(g, 2)))))
            if(abs(d1) > abs(d2)):
                a = (e-i) / d1
            else:
                a = (e-i) / d2
            a1 = a0 - a
            if(abs(a1 - a0) < epsilon):
                return a0
            a0 = a1
            j = j+1


# NEW ASSIGNMENT      NEW ASSIGNMENT       NEW ASSIGNMENT      NEW ASSIGNMENT      NEW ASSIGNMENT      NEW ASSIGNMENT       NEW ASSIGNMENT


# 19. Midpoint
def midpoint(a, b, fun, N):
    h = (b - a)/N
    # print("h = ", h)
    sum = 0
    for i in range(1, N+1):
        xi = ((a + (i-1)*h) + (a + i*h))/2
        area = h * fun(xi)
        sum = sum + area
        # print("sum = ", sum)
    return sum


# 20. Traphezoidal
def traphezoidal(a, b, fun, N):
    h = (b - a)/N
    sum = 0
    for i in range(N):
        x0 = a + i*h
        x1 = a + (i + 1)*h
        area = h/2*(fun(x0) + fun(x1))
        sum = sum + area
        # print("sum = ", sum)
    return sum


# 21. Simpson
def simpson(a, b, fun, N):
    # due to odd no. issue with simpson method we take N=(Even no.)
    if (N % 2) != 0:
        N = N + 1
        print("Due to odd no. issue with simpson method, we take N=(N+1) i.e N =", N)
    h = (b - a)/N
    sum = 0
    for i in range(0, N, 2):
        x0 = a + i*h
        x2 = a + (i+2)*h
        h1 = (x2 - x0)/2
        x1 = (x2 + x0)/2
        intg = (h1/3)*(fun(x0) + 4*fun(x1) + fun(x2))
        sum = sum + intg
    return sum


# 22. Errors
def max_error_midpoint(a, b, sec_der_f_max, max_error):
    err = (math.sqrt((((b-a)**3)*abs(sec_der_f_max))/(24*max_error)))
    return math.ceil(err)


def max_error_trapezoidal(a, b, sec_der_f_max, max_error):
    err = (math.sqrt((((b-a)**3)*abs(sec_der_f_max))/(12*max_error)))
    return math.ceil(err)


def max_error_simpson(a, b, four_der_f_max, max_error):
    err = (((((b-a)**5)*abs(four_der_f_max))/(180*max_error))**(1/4))
    return math.ceil(err)


# 23.Monte-Carlo
def monte_carlo(a, b, fun, N, file):
    # print(" {:<12}| {:<20}".format("N", "Integral (Value of pi)"))
    Fn = 0
    sum_fx = 0
    # print("\nN = ", N)
    for i in range(N):
        x = random.random()
        x = a + ((b - a)*x)
        fx = fun(x)
        sum_fx = sum_fx + fx
        Fn = ((b - a)/(i+1)) * sum_fx
        # print("Integration of the function = ", Fn)
        # print(" {:<12}| {:<20}".format((i+1), Fn))
        file.write("{:<15}{:<20}\n".format((i+1), Fn))
    # print("Integration of the function = ", Fn)
    file.close()
    return Fn


# 24. Euler's Forward
def explicit_euler(fun, x, y, xlimit):
    h = 0.3
    i = 0
    while(x[i] < xlimit):
        i = i + 1
        x.append(x[i-1] + h)
        y.append(y[i-1] + h * fun(y[i-1], x[i-1]))


# 25. Runge-Kutta Method
def runge_kutta(fy, fz, x, y, z, xlimit, h, txt_file):
    file = open(txt_file, "w")
    while(x < xlimit):
        file.write(
            "%5.21f                %5.21f                %5.21f\n" % (x, y, z))
        k1y = h * fy(z, x)
        k1z = h * fz(y, z, x)

        k2y = h * fy(z + (k1z / 2), x + (h / 2))
        k2z = h * fz(y + (k1y / 2), z, x + (h / 2))

        k3y = h * fy(z + (k2z / 2), x + (h / 2))
        k3z = h * fz(y + (k2y / 2), z, x + (h / 2))

        k4y = h * fy(z + k3z, x + h)
        k4z = h * fz(y + k3y, z, x + h)

        y = y + (1 / 6) * (k1y + 2 * k2y + 2 * k3y + k4y)
        z = z + (1 / 6) * (k1z + 2 * k2z + 2 * k3z + k4z)
        x = x + h
    file.write("%f  %lf %lf\n" % (x, y, z))
    file.close()
    return y, xlimit


# 26. Shooting Method
def shooting_method(fy, fz, x, xlimit, y, yn, zl, zh, h, txt_file):
    z0 = zl
    for i in range(50):
        txt_filel = "%s_l%i.txt" % (txt_file, i)
        y_el, xl = runge_kutta(fy, fz, x, y, z0, xlimit, h,  txt_filel)
        if abs(y_el - yn) < 10 ** (-6):
            return y_el, z0
        else:
            txt_fileh = "%s_h%i.txt" % (txt_file, i)
            z0 = zh
            y_eh, xh = runge_kutta(fy, fz, x, y, z0, xlimit, h, txt_fileh)
            if abs(y_eh - yn) < 10 ** (-6):
                return y_eh, z0
            elif y_el < yn and yn < y_eh:
                z0 = zl + (zh - zl) * (yn - y_el) / (y_eh - y_el)
            elif y_eh < yn and yn < y_el:
                z0 = zh + (zl - zh) * (yn - y_eh) / (y_el - y_eh)
            else:
                print("Chosse differnt values of z(%.0f)" % (x))
                return None, None


# 27. Random Walk


def random_walk(M, N):

    random.seed(None)
    r2 = 0
    R2 = []
    X = []
    Y = []
    sum_r2 = 0
    for j in range(0, M):

        X1 = []
        Y1 = []
        x = 0.0
        y = 0.0
        r2 = 0.0
        X1.append(x)
        Y1.append(y)

        for i in range(0, N):
            theta = 2 * math.pi * random.random()
            x1 = math.cos(theta)
            y1 = math.sin(theta)
            x = x + x1
            y = y + y1
            X1.append(x)
            Y1.append(y)
        X.append(X1)
        Y.append(Y1)
        r2 = x ** 2 + y ** 2
        R2.append(r2)
    sum_r2 = 0
    for i in range(len(R2)):
        sum_r2 = sum_r2 + R2[i]

    avg_r2 = sum_r2 / len(R2)
    r_rms = math.sqrt(avg_r2)

    sum_x = 0
    sum_y = 0
    for i in range(len(X)):
        sum_x = sum_x + X[i][len(X[i]) - 1]
        sum_y = sum_y + Y[i][len(Y[i]) - 1]

    avg_x = sum_x / len(X)
    avg_y = sum_y / len(Y)
    rad_dis = math.sqrt(avg_x ** 2 + avg_y ** 2)

    return X, Y, r_rms, avg_x, avg_y, rad_dis


# 28.  Monte Carlo Volume
def monte_carlo_volume(a1, a2, b1, b2, c1, c2, fun, N, analyt_val):
    X1 = []
    Y1 = []
    Z1 = []
    vol_box = (a2 - a1) * (b2 - b1) * (c2 - c1)
    Fn = 0
    inte = 0

    for i in range(N):
        x = random.uniform(a1, a2)
        y = random.uniform(b1, b2)
        z = random.uniform(c1, c2)

        if (fun(x, y, z) <= 1):
            X1.append(x)
            Y1.append(y)
            Z1.append(z)
            inte = inte + 1
    Fn = (vol_box/float(N)) * inte
    frac_err = abs(Fn - analyt_val)/analyt_val
    return Fn, X1, Y1, Z1, frac_err

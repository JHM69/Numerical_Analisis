from math import sin, pi
def trapezoidal(f, a, b, n):
    h = float(b-a)/n;
    result= (h * (f(a) + f(b)) )/2;
    for i in range(1, n):
        xi = a + i*h;
        result +=  h*f(xi);
    return result

f = lambda x: sin(x)
n = 4 
print(trapezoidal(f, 0, pi/2, n))


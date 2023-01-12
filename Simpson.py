import math
f = lambda x: math.sin(x)

def simpson13(f, a, b, n):
    h = float(b-a)/n
    result= (h*(f(a)+f(b))) / 3
    for i in range(1, n):
        xi = a + i*h
        if i % 2 == 0:
            result += (2 * h * f(xi) )/3
        else :
            result += (4 * h * f(xi) )/3
    return result

n = 4 
print(simpson13(f, 0, math.pi/2, n))
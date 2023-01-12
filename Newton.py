# importing "math" for mathematical operations
import math

def Newton(f,f1,p0,TOL,N0):
    i=1;
    print('n','  ','        p0','  ','             p-p0');
    while i<=N0:
        p = p0-f(p0)/f1(p0);
        print(format(i),'  ',format(p0, "10.3f"),'  ',format(abs(p-p0), "10.3e"));
        if abs(p-p0)< TOL:
            return print('The solution is ', p);
        i=i+1;
        p0=p;
    print('The method fails after N0 iterations');
    return None

f = lambda x: math.cos(x) - x;
f1 = lambda x: - math.sin(x) - 1;
Newton(f, f1, math.pi/4, 0.0000000000000001, 20)


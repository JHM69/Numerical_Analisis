def bisection(f,a,b,TOL,N0):
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    i=1
    FA = f(a)
    print('   n','         a','             b','             c','            f(c)')
    while i<=N0:
        c = ( a+b ) / 2
        FP = f(c)
        print(format(i,'>4d'),' ', format(a,'>12.8f'),' ', format(b,'>12.8f'),' ', format(c,'>12.8f'),' ', format(f(c),'>12.2e'))
        if FP == 0 or abs(FP)< TOL:
            return print('The solution is ', c)
        i=i+1
        if FA*FP>0:
            a=c
        else:
            b=c
    print('The method fails after N0 iterations')
    return None

f = lambda x: x**3+4*x**2 - 10
bisection(f,1,2,.00001,25)
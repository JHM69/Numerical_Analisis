import math
f = lambda x: x*math.exp(x);
h = 0.2;
x = 2.0;

Df_x0 = (-3*(f(x))+4*(f(x+h))-(f(x+2*h)))/(2*h);

print("Value using 3 point end point : ",   format(Df_x0,'>10.2e'))

Df_x0 = ((f(x+h))-(f(x-h)))/(2*h);

print('The derivative of f at x (By three-point midpoint formula):\n',  format(Df_x0,'>12.2e'));

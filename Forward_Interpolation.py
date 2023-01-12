
def u_cal(u, n):
    for i in range(1, n):
        u = u * (u - i)
    return u

def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)


n = 4;
x = [45, 50, 55, 60];


y = [[0 for i in range(n)]
     for j in range(n)];
y[0][0] = 0.7071;
y[1][0] = 0.7660;
y[2][0] = 0.8192;
y[3][0] = 0.8660;


for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];

for i in range(n):
    print(x[i], end="\t");
    for j in range(n - i):
        print( format(y[i][j], "10.4f"), end="\t");
    print("");


value = 52;

sum = y[0][0];
u = (value - x[0]) / (x[1] - x[0]);

for i in range(1, n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i);

print("\nValue at", value,
      "is", round(sum, 6));
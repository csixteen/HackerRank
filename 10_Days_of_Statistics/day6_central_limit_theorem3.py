from math import erf, sqrt

def F(x, u, std_dev):
    return 0.5*(1 + erf((x-u)/(std_dev*(2**0.5))))

n = int(input())
u = int(input())
std_dev = int(input()) / sqrt(n)
x = float(input())
z = float(input())

print(round(u - z*std_dev, 2))
print(round(u + z*std_dev, 2))

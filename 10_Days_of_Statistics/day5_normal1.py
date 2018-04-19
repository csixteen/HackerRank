from math import erf, sqrt

def F(x, u, std_dev):
    return (1.0 + erf((x-u) / (std_dev * sqrt(2.0)))) / 2.0

u, std_dev = map(float, input().split(" "))
print(F(float(input()), u, std_dev))
A, B = map(float, input().split(" "))
print(F(B, u, std_dev) - F(A, u, std_dev))

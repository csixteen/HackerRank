from math import erf, sqrt

def F(x, u, std_dev):
    return (1.0 + erf((x-u) / (std_dev * sqrt(2.0)))) / 2.0

u, std_dev = map(float, input().split(" "))
first = float(input())
threshold = float(input())
print(round((1 - F(first, u, std_dev)) * 100, 2))
print(round((1 - F(threshold, u, std_dev)) * 100, 2))
print(round((F(threshold, u, std_dev) - F(0, u, std_dev)) * 100, 2))

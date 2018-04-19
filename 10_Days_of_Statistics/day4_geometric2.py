def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

num, den = map(int, input().split(" "))
n = int(input())
print(round(sum([b(i, n, num/den) for i in range(1, n+1)]), 3))

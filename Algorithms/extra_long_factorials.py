def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

N = int(input())
print(fact(N))

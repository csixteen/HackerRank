t = int(input())
for i in range(t):
    n = int(input())
    s = n * (n + 1) // 2
    sq = (2*n + 1) * (n + 1) * n // 6
    print((s**2) - sq)

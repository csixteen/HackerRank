t = int(input())
for i in range(t):
    n, m, s = map(int, input().split(" "))
    print((s + m - 2) % n + 1)

n, d = map(int, input().split())
a = input().split()
print(" ".join(a[d:] + a[:d]))

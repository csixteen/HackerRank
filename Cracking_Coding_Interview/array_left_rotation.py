n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
print(" ".join([str(a[i % n]) for i in range(k, n+k)]))

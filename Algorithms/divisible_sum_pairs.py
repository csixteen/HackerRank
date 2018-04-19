n, k = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
print(len([1 for i in range(n) for j in range(n) if i < j and not ((a[i]+a[j]) % k)]))

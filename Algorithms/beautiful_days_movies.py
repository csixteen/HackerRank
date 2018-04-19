i, j, k = map(int, input().split(" "))
print(len([1 for n in range(i, j+1) if not (abs(n - int(str(n)[::-1])) % k)]))

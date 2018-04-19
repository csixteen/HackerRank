n, a = int(input()), input().split(" ")
s = sorted([1 + a[i+1:].index(e) for i,e in enumerate(a) if i < n-1 and a[i+1:].count(e)])
print(-1 if len(s) == 0 else s[0])

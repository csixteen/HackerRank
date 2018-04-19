t1, t2, n = map(int, input().split(" "))
for i in range(2, n):
    tn = t1 + t2**2
    t1, t2 = t2, tn
print(tn)

x1, v1, x2, v2 = map(int, input().strip().split(' '))
if v1 == v2:
    print("NO")
else:
    j = (x1 - x2) // (v2 - v1)
    print("YES" if j > 0 and (x1+v1*j == x2+v2*j) else "NO")

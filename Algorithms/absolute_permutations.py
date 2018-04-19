for _ in range(int(input())):
    n, k = map(int, input().split(" "))
    l = list(range(1, n+1))
    if k == 0:
        print(" ".join(map(str, l)))
    elif (n % 2) or ((not n % 2) and (n % k)):
        print(-1)
    else:
        for i in range(0, len(l)-k, k*2):
            l[i:i+k],l[i+k:i+2*k] = l[i+k:i+2*k], l[i:i+k]
        print(" ".join(map(str, l)))

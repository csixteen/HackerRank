def deletions(w):
    d = 0
    p = w[0]
    for c in w[1:]:
        if c == p:
            d += 1
        p = c
    return d

N = int(input())
for i in range(N):
    print(deletions(input()))

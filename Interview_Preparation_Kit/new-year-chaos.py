def minimum_bribes(q):
    total = 0
    N = len(q)
    for i in range(N-1, -1, -1):
        if q[i] - (i+1) > 2:
            return 'Too chaotic'
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                total += 1

    return total

q = [2, 1, 4, 3, 5, 7, 6, 10, 8, 9]
print(minimum_bribes(q))

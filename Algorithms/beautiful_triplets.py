n, d = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
triplets = 0
for i in range(n-2):
    j = i+1
    while (j < n) and (a[j] - a[i] < d):
        j += 1

    if (j >= n-1) or (a[j] - a[i] > d):
        continue

    k = j+1
    while (k < n) and (a[k] - a[j] < d):
        k += 1

    if (k == n) or (a[k] - a[j] > d):
        continue

    triplets += 1

print(triplets)

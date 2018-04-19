from operator import itemgetter

def get_flavors(flavors, m, n):
    candidates = sorted(list(enumerate(flavors, 1)), key=itemgetter(1))
    i, j = 0, n-1
    min_e, max_e = candidates[i], candidates[j]
    c = min_e[1] + max_e[1]
    while c != m:
        if max_e[1] >= m:
            j -= 1
            max_e = candidates[j]
        elif min_e[1] < m - max_e[1]:
            i += 1
            min_e = candidates[i]
        else:
            j -= 1
            max_e = candidates[j]

        c = min_e[1] + max_e[1]

    return sorted([min_e[0], max_e[0]])

for t in range(int(input())):
    m = int(input())
    n = int(input())
    flavors = list(map(int, input().split(" ")))

    print(" ".join(map(str, get_flavors(flavors, m, n))))

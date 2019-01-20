from collections import Counter, defaultdict


def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0

    for v in arr:
        if v in r3:
            count += r3[v]

        if v in r2:
            r3[v*r] += r2[v]

        r2[v*r] += 1

    return count


def countTriplets2(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0

    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1

    return count


if __name__ == '__main__':
    _, r = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(countTriplets(arr, r))


# coding: utf-8
from array import array
from bisect import insort, bisect_left


def ki_sort(arr, d):
    R = max(arr) + 2
    freq = array('I', [0] * R)

    for n in arr:
        freq[n+1] += 1

    for i in range(R-1):
        freq[i+1] += freq[i]

    aux = array('I', [0] * d)
    for n in arr:
        aux[freq[n]] = n
        freq[n] += 1

    return aux


def fraudulent_activity(arr, n, d):
    mv = array('I', arr)
    trail = ki_sort(mv[:d], d)
    total = 0

    for i, curr in enumerate(mv[d:]):
        to_remove = mv[i]
        if (d % 2 == 0) and (curr >= trail[d>>1] + trail[(d>>1) - 1]):
            total += 1
        elif curr >= trail[d>>1] << 1:
            total += 1
        j = bisect_left(trail, to_remove)
        del trail[j]
        insort(trail, curr)

    return total


if __name__ == '__main__':
    n, d = list(map(int, input().split()))
    expenses = list(map(int, input().split()))
    print(fraudulent_activity(expenses, n, d))


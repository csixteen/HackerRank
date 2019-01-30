# coding: utf-8
from array import array


def mean(arr, d):
    if d % 2 == 0:
        return (arr[(d // 2)-1] + arr[d // 2]) / 2
    else:
        return arr[d // 2]


def ki_sort(arr, mx, d):
    R = mx + 2
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
    mv = memoryview(array('I', arr))
    mx = max(mv)
    trail = ki_sort(mv[:d], mx, d)
    m = mean(trail, d)
    total = 0

    for i in range(d, n):
        trail = ki_sort(mv[i-d:i], mx, d)
        m = mean(trail, d)
        if arr[i] >= 2*m:
            total += 1

    return total


if __name__ == '__main__':
    n, d = list(map(int, input().split()))
    expenses = list(map(int, input().split()))
    print(fraudulent_activity(expenses, n, d))


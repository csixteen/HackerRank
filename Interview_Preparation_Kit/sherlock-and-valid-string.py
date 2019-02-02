#!/usr/bin/env python3
# coding: utf-8
from collections import Counter


def is_valid(s):
    freq = Counter()
    inv = Counter()

    for c in s:
        freq[c] += 1
        inv[freq[c]-1] -= 1
        if inv[freq[c]-1] <= 0:
            del inv[freq[c]-1]
        inv[freq[c]] += 1

    if len(inv) == 1:
        return 'YES'
    elif len(inv) > 2:
        return 'NO'

    x = sorted(inv.most_common(2))
    if x[0] == (1,1):
        return 'YES'
    elif abs(x[0][0]-x[1][0]) > 1:
        return 'NO'
    elif x[1][0] > x[0][0] and x[1][1] == 1:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    print(is_valid(input()))


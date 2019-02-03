#!/usr/bin/env python3
# coding: utf-8
import unittest


def substr_count(n, s):
    if n == 1:
        return 1

    total = 0
    prev = s[0]
    prev_len = 1
    for i in range(1, n):
        if s[i] != prev:
            total += ((prev_len * (prev_len + 1)) >> 1)
            prev_len = 1
            prev = s[i]
        else:
            prev_len += 1

    total += ((prev_len * (prev_len + 1)) >> 1)

    for i in range(1, n-1):
        if s[i] != s[i-1] and s[i-1] == s[i+1]:
            total += 1
            j = 1
            while i-1-j >= 0 and i+1+j < n:
                if s[i-1-j] == s[i-1] and s[i+1+j] == s[i+1]:
                    total += 1
                    j += 1
                else:
                    break

    return total


class TestSubstrCount(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ((8, 'mnonopoo'), 12),
            ((5, 'asasd'), 7),
            ((7, 'abcbaba'), 10),
            ((4, 'aaaa'), 10),
            ((7, 'aaaabbb'), 16)
        ]

    def test_substr_count(self):
        for inputs, result in self.test_cases:
            self.assertEqual(result, substr_count(*inputs))


if __name__ == '__main__':
    unittest.main()


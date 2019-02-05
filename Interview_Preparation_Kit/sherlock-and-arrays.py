#!/usr/bin/env python3
# coding: utf-8
import unittest


def balanced_sums(arr):
    total = sum(arr)
    so_far = 0
    for i in arr:
        if total - i == 2*so_far:
            return 'YES'
        else:
            so_far += i

    return 'NO'


class TestBalancedSums(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 2, 3], 'NO'),
            ([1, 2, 3, 3], 'YES'),
            ([1, 1, 4, 1, 1], 'YES'),
            ([2, 0, 0, 0], 'YES'),
            ([0, 0, 2, 0], 'YES')
        ]

    def test_balanced_sums(self):
        for arr, expected in self.test_cases:
            self.assertEqual(expected, balanced_sums(arr))


if __name__ == '__main__':
    unittest.main()


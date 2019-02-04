#!/usr/bin/env python3
# coding: utf-8
import unittest


def count_pairs(n, k, numbers):
    numbers = sorted(numbers)
    i = 0
    j = 1
    total = 0
    while j < n:
        x = numbers[j]-numbers[i]
        if x < k:
            j += 1
        elif x > k:
            i += 1
        else:
            total += 1
            j += 1

    return total


def count_pairs2(n, k, numbers):
    return len(set(numbers) & set(x + k for x in numbers))


class TestCountPairs(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ((4, 1, [1,2,3,4]), 3),
            ((5, 2, [1, 5, 3, 4, 2]), 3),
            ((11, 3, [17, 16, 2, 4, 3, 8, 10, 6, 7, 11, 13]), 6)
        ]

    def test_count_pairs(self):
        for inputs, expected in self.test_cases:
            self.assertEqual(count_pairs(*inputs), expected)
            self.assertEqual(count_pairs2(*inputs), expected)


if __name__ == '__main__':
    unittest.main()


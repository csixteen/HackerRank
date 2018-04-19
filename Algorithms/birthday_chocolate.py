class Solution(object):
    @staticmethod
    def different_ways(n, pieces, d, m):
        ways = 0
        for i in range(n):
            if sum(pieces[i:i+m]) == d:
                ways += 1

        return ways


import unittest

class SolutionTest(unittest.TestCase):
    def test_different_ways(self):
        self.assertEqual(2, Solution.different_ways(5, [1, 2, 1, 3, 2], 3, 2))
        self.assertEqual(0, Solution.different_ways(6, [1, 1, 1, 1, 1, 1], 3, 2))
        self.assertEqual(5, Solution.different_ways(6, [1, 1, 1, 1, 1, 1], 2, 2))
        self.assertEqual(1, Solution.different_ways(1, [4], 4, 1))


if __name__ == "__main__":
    unittest.main()


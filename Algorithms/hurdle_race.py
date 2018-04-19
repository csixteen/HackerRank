class Solution(object):
    @staticmethod
    def hurdle_race(n, k, heights):
        return max(0, max(heights) - k)


import unittest

class SolutionTest(unittest.TestCase):
    def test_hurdle_race(self):
        self.assertEqual(2, Solution.hurdle_race(5, 4, [1, 6, 3, 5, 2]))
        self.assertEqual(0, Solution.hurdle_race(5, 7, [2, 5, 4, 5, 2]))

if __name__ == "__main__":
    unittest.main()


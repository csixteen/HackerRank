class Solution(object):
    @staticmethod
    def electronics_shop(s, n, m, keyboards, usbs):
        keyboards = sorted(keyboards, reverse=True)
        usbs = sorted(usbs)
        j, max_value = 0, -1
        for i in range(n):
            while j < m:
                if keyboards[i] + usbs[j] > s:
                    break
                elif keyboards[i] + usbs[j] > max_value:
                    max_value = keyboards[i] + usbs[j]
                j += 1

        return max_value


import unittest

class SolutionTest(unittest.TestCase):
    def test_electronics_shop(self):
        self.assertEqual(9, Solution.electronics_shop(10, 2, 3, [3, 1], [5, 2, 8]))
        self.assertEqual(-1, Solution.electronics_shop(5, 1, 1, [4], [5]))

if __name__ == "__main__":
    unittest.main()


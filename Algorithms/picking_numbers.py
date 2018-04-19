class Solution(object):
    @staticmethod
    def picking_numbers(n, numbers):
        if n == 1:
            return 1

        total, n_curr = 1, 1
        numbers = sorted(numbers)
        current = [numbers[0]]
        for i in range(1, n):
            if numbers[i] - current[0] <= 1:
                current.append(numbers[i])
                n_curr += 1
            else:
                if n_curr > total:
                    total = n_curr
                current = [numbers[i]]
                n_curr = 1

        return max(total, n_curr)


import unittest

class SolutionTest(unittest.TestCase):
    def test_picking_numbers(self):
        self.assertEqual(3, Solution.picking_numbers(6, [4, 6, 5, 3, 3, 1]))
        self.assertEqual(5, Solution.picking_numbers(6, [1, 2, 2, 3, 1, 2]))
        self.assertEqual(6, Solution.picking_numbers(6, [1, 1, 1, 1, 1, 1]))
        self.assertEqual(1, Solution.picking_numbers(6, [1, 3, 5, 7, 9, 11]))

if __name__ == "__main__":
    unittest.main()


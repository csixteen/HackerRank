class Solution(object):
    @staticmethod
    def drawing_book(n, p):
        if p <= n // 2:
            return p // 2
        elif n % 2 == 0:
            return ((n - p) // 2) + (n - p) % 2
        else:
            return (n - p) // 2


import unittest

class SolutionTest(unittest.TestCase):
    def test_drawing_book(self):
        self.assertEqual(0, Solution.drawing_book(2, 1))
        self.assertEqual(1, Solution.drawing_book(6, 2))
        self.assertEqual(1, Solution.drawing_book(6, 4))
        self.assertEqual(0, Solution.drawing_book(5, 4))
        self.assertEqual(0, Solution.drawing_book(6, 6))
        self.assertEqual(4, Solution.drawing_book(21, 8))
        self.assertEqual(4, Solution.drawing_book(21, 13))
        self.assertEqual(1, Solution.drawing_book(7, 3))
        self.assertEqual(1, Solution.drawing_book(6, 5))

if __name__ == "__main__":
    unittest.main()

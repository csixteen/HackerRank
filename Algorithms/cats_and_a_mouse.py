class Solution(object):
    @staticmethod
    def cats_mouse(x, y, z):
        if abs(x-z) < abs(y-z):
            return "Cat A"
        elif abs(y-z) < abs(x-z):
            return "Cat B"
        else:
            return "Mouse C"


import unittest

class SolutionTest(unittest.TestCase):
    def test_cats_mouse(self):
        self.assertEqual("Cat B", Solution.cats_mouse(1, 2, 3))
        self.assertEqual("Mouse C", Solution.cats_mouse(1, 3, 2))
        self.assertEqual("Cat A", Solution.cats_mouse(2, 1, 3))

if __name__ == "__main__":
    unittest.main()


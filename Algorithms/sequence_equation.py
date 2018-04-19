class Solution(object):
    @staticmethod
    def sequence_equation(n, sequence):
        px_x = {px: x for x, px in enumerate(sequence, 1)}
        return [px_x[px_x[x]] for x in range(1, n + 1)]


import unittest

class SolutionTest(unittest.TestCase):
    def test_sequence_equation(self):
        self.assertListEqual(
            [2, 3, 1],
            Solution.sequence_equation(3, [2, 3, 1])
        )

if __name__ == "__main__":
    unittest.main()


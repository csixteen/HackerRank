class Solution(object):
    MAGIC_SQUARES = [
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8]
    ]

    def magic_square(self, s):
        totals = []
        for ms in self.MAGIC_SQUARES:
            totals.append(sum([abs(ms_e - s_e) for ms_e, s_e in zip(ms, s)]))

        return min(totals)

import unittest

class SolutionTest(unittest.TestCase):
    def test_magic_square(self):
        s = Solution()
        self.assertEqual(0, s.magic_square([6, 1, 8, 7, 5, 3, 2, 9, 4]))
        self.assertEqual(1, s.magic_square([4, 9, 2, 3, 5, 7, 8, 1, 5]))
        self.assertEqual(4, s.magic_square([4, 8, 2, 4, 5, 7, 6, 1, 6]))
        self.assertEqual(45, s.magic_square([0, 0, 0, 0, 0, 0, 0, 0, 0]))
        self.assertEqual(36, s.magic_square([9, 9, 9, 9, 9, 9, 9, 9, 9]))

if __name__ == "__main__":
    unittest.main()

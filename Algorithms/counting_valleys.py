class Solution(object):
    @staticmethod
    def counting_valleys(steps, seq):
        valleys, level = 0, 0
        for direction in seq:
            level += 1 if direction == 'U' else -1
            if level == 0 and direction == 'U':
                valleys += 1

        return valleys


import unittest

class SolutionTest(unittest.TestCase):
    def test_counting_valleys(self):
        self.assertEqual(1, Solution.counting_valleys(8, 'UDDDUDUU'))
        self.assertEqual(0, Solution.counting_valleys(6, 'UUUDDD'))
        self.assertEqual(2, Solution.counting_valleys(12, 'DDUUUUDDDDUU'))

if __name__ == "__main__":
    unittest.main()

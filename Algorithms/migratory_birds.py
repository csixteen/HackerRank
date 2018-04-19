from collections import Counter
from operator import itemgetter

class Solution(object):
    @staticmethod
    def migratory_birds(n, birds):
        c = Counter(birds)
        b = sorted(c.items(), key=itemgetter(1, 0), reverse=True)
        bird_type, count = b[0]
        if len(b) > 1:
            for i in range(1, len(b)):
                if b[i][1] < count:
                    break
                else:
                    bird_type, count = b[i]

        return bird_type


import unittest

class SolutionTest(unittest.TestCase):
    def test_migratory_birds(self):
        self.assertEqual(4, Solution.migratory_birds(6, [1, 4, 4, 4, 5, 3]))
        self.assertEqual(2, Solution.migratory_birds(9, [1, 4, 4, 4, 5, 2, 2, 2, 3]))
        self.assertEqual(1, Solution.migratory_birds(1, [1]))
        self.assertEqual(1, Solution.migratory_birds(9, [9, 8, 3, 2, 1, 5, 6, 7, 4]))

if __name__ == "__main__":
    unittest.main()

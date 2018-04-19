class Solution(object):
    @staticmethod
    def generate_ranks(scores):
        i, ranks = 1, {}
        for s in scores:
            if s in ranks:
                continue
            else:
                ranks[s] = i
                i += 1

        return ranks

    @staticmethod
    def get_rank(level, n, scores, ranks, previous_i = None):
        if level >= scores[0]:
            return previous_i, 1

        i = previous_i or n - 1
        while level > scores[i] and i >= 0:
            i -= 1

        if i > 0:
            previous_i = i

        return (previous_i, ranks[scores[i]] if scores[i] == level else ranks[scores[i]] + 1)


    @staticmethod
    def climbing(n, scores, l, levels):
        c = []
        ranks = Solution.generate_ranks(scores)
        previous_i = None
        for level in levels:
            previous_i, rank = Solution.get_rank(level, n, scores, ranks, previous_i)
            c.append(rank)

        return c


import unittest

class SolutionTest(unittest.TestCase):
    def test_generate_ranks(self):
        self.assertDictEqual(
            {100: 1, 90: 2, 80: 3},
            Solution.generate_ranks([100, 90, 90, 80])
        )
        self.assertDictEqual(
            {100: 1, 50: 2, 40: 3, 20: 4, 10: 5},
            Solution.generate_ranks([100, 100, 50, 40, 40, 20, 10])
        )

    def test_get_rank(self):
        self.assertEqual(
            (6, 6),
            Solution.get_rank(
                5,
                7,
                [100, 100, 50, 40, 40, 20, 10],
                {100: 1, 50: 2, 40: 3, 20: 4, 10: 5}
            )
        )

    def test_climbing(self):
        self.assertListEqual(
            [6, 4, 2, 1],
            Solution.climbing(7, [100, 100, 50, 40, 40, 20, 10], 4, [5, 25, 50, 120])
        )

if __name__ == "__main__":
    unittest.main()


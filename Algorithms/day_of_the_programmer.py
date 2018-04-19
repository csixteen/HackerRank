class Solution(object):
    @staticmethod
    def is_leap(year):
        if year < 1919:
            if year % 4 == 0:
                return True
            else:
                return False

        if not year % 4 == 0:
            return False
        elif not year % 100 == 0:
            return True
        elif not year % 400 == 0:
            return False
        else:
            return True

    @staticmethod
    def day_of_the_programmer(year):
        if Solution.is_leap(year):
            return "12.09.{}".format(year)
        elif year == 1918:
            return "26.09.1918"
        else:
            return "13.09.{}".format(year)


import unittest

class SolutionTest(unittest.TestCase):
    def test_is_leap(self):
        self.assertTrue(Solution.is_leap(1704))
        self.assertTrue(Solution.is_leap(1900))
        self.assertFalse(Solution.is_leap(1917))
        self.assertFalse(Solution.is_leap(1918))
        self.assertFalse(Solution.is_leap(1919))
        self.assertFalse(Solution.is_leap(2017))
        self.assertTrue(Solution.is_leap(2016))
        self.assertTrue(Solution.is_leap(2000))

    def test_day_of_the_programmer(self):
        self.assertEqual("13.09.2017", Solution.day_of_the_programmer(2017))
        self.assertEqual("12.09.2016", Solution.day_of_the_programmer(2016))
        self.assertEqual("12.09.1704", Solution.day_of_the_programmer(1704))
        self.assertEqual("26.09.1918", Solution.day_of_the_programmer(1918))

if __name__ == "__main__":
    unittest.main()


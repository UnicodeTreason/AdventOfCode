import unittest

from solutions.year2015.day04 import calculate


class TestSum(unittest.TestCase):

    def test_year2015_day04_input01(self):
        """
        Compare test input to provided true answer
        """
        testData = 'abcdef'
        result = calculate(testData)
        self.assertEqual(result, 609043)

    def test_year2015_day04_input02(self):
        """
        Compare test input to provided true answer
        """
        testData = 'pqrstuv'
        result = calculate(testData)
        self.assertEqual(result, 1048970)

    def test_year2015_day04_input03(self):
        """
        Compare test input to provided true answer
        """
        testData = 'yzbqklnj'
        result = calculate(testData, True)
        self.assertEqual(result, 9962624)


if __name__ == '__main__':
    unittest.main()

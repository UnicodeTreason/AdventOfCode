import unittest

from adventofcode.year2015.day02 import calculate


class TestSum(unittest.TestCase):

    def test_year2015_day02_input01(self):
        """
        Compare test input to provided true answer
        """
        testData = ['2x3x4']
        result = calculate(testData)
        self.assertEqual(result, 58)

    def test_year2015_day02_input02(self):
        """
        Compare test input to provided true answer
        """
        testData = ['1x1x10']
        result = calculate(testData)
        self.assertEqual(result, 43)

    def test_year2015_day02_input03(self):
        """
        Compare test input to provided true answer
        """
        testData = ['2x3x4', '1x1x10']
        result = calculate(testData)
        self.assertEqual(result, 101)

    def test_year2015_day02_input04(self):
        """
        Compare test input to provided true answer
        """
        testData = ['2x3x4']
        result = calculate(testData, True)
        self.assertEqual(result, 34)

    def test_year2015_day02_input05(self):
        """
        Compare test input to provided true answer
        """
        testData = ['1x1x10']
        result = calculate(testData, True)
        self.assertEqual(result, 14)

    def test_year2015_day02_input06(self):
        """
        Compare test input to provided true answer
        """
        testData = ['2x3x4', '1x1x10']
        result = calculate(testData, True)
        self.assertEqual(result, 48)


if __name__ == '__main__':
    unittest.main()

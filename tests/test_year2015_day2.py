import unittest

from solutions.year2015.day2 import calculate


class TestSum(unittest.TestCase):

    def test_year2015_day2_input1(self):
        """
        Compare test input to provided true answer
        """
        testData = ['2x3x4']
        result = calculate(testData)
        self.assertEqual(result, 58)

    def test_year2015_day2_input2(self):
        """
        Compare test input to provided true answer
        """
        testData = ['1x1x10']
        result = calculate(testData)
        self.assertEqual(result, 43)

    def test_year2015_day2_input3(self):
        """
        Compare test input to provided true answer
        """
        testData = ['2x3x4', '1x1x10']
        result = calculate(testData)
        self.assertEqual(result, 101)


if __name__ == '__main__':
    unittest.main()

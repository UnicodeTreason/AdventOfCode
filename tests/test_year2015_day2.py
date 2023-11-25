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

    def test_year2015_day2_input4(self):
        """
        Compare test input to provided true answer
        """
        testData = ['2x3x4']
        result = calculate(testData, True)
        self.assertEqual(result, 34)

    def test_year2015_day2_input5(self):
        """
        Compare test input to provided true answer
        """
        testData = ['1x1x10']
        result = calculate(testData, True)
        self.assertEqual(result, 14)

    def test_year2015_day2_input6(self):
        """
        Compare test input to provided true answer
        """
        testData = ['2x3x4', '1x1x10']
        result = calculate(testData, True)
        self.assertEqual(result, 48)


if __name__ == '__main__':
    unittest.main()

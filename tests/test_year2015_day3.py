import unittest

from solutions.year2015.day3 import calculate


class TestSum(unittest.TestCase):

    def test_year2015_day3_input1(self):
        """
        Compare test input to provided true answer
        """
        testData = '>'
        result = calculate(testData)
        self.assertEqual(result, 2)

    def test_year2015_day3_input2(self):
        """
        Compare test input to provided true answer
        """
        testData = '^>v<'
        result = calculate(testData)
        self.assertEqual(result, 4)

    def test_year2015_day3_input3(self):
        """
        Compare test input to provided true answer
        """
        testData = '^v^v^v^v^v'
        result = calculate(testData)
        self.assertEqual(result, 2)

    def test_year2015_day3_input4(self):
        """
        Compare test input to provided true answer
        """
        testData = '^v'
        result = calculate(testData, True)
        self.assertEqual(result, 3)

    def test_year2015_day3_input5(self):
        """
        Compare test input to provided true answer
        """
        testData = '^>v<'
        result = calculate(testData, True)
        self.assertEqual(result, 3)

    def test_year2015_day3_input6(self):
        """
        Compare test input to provided true answer
        """
        testData = '^v^v^v^v^v'
        result = calculate(testData, True)
        self.assertEqual(result, 11)

if __name__ == '__main__':
    unittest.main()

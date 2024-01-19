import unittest

from solutions.year2015.day01 import calculate


class TestSum(unittest.TestCase):

    def test_year2015_day01_input01(self):
        """
        Compare test input to provided true answer
        """
        testData = '(())'
        result = calculate(testData)
        self.assertEqual(result, 0)

    def test_year2015_day01_input02(self):
        """
        Compare test input to provided true answer
        """
        testData = '()()'
        result = calculate(testData)
        self.assertEqual(result, 0)

    def test_year2015_day01_input03(self):
        """
        Compare test input to provided true answer
        """
        testData = '((('
        result = calculate(testData)
        self.assertEqual(result, 3)

    def test_year2015_day01_input04(self):
        """
        Compare test input to provided true answer
        """
        testData = '(()(()('
        result = calculate(testData)
        self.assertEqual(result, 3)

    def test_year2015_day01_input05(self):
        """
        Compare test input to provided true answer
        """
        testData = '))((((('
        result = calculate(testData)
        self.assertEqual(result, 3)

    def test_year2015_day01_input06(self):
        """
        Compare test input to provided true answer
        """
        testData = '())'
        result = calculate(testData)
        self.assertEqual(result, -1)

    def test_year2015_day01_input07(self):
        """
        Compare test input to provided true answer
        """
        testData = '))('
        result = calculate(testData)
        self.assertEqual(result, -1)

    def test_year2015_day01_input08(self):
        """
        Compare test input to provided true answer
        """
        testData = ')))'
        result = calculate(testData)
        self.assertEqual(result, -3)

    def test_year2015_day01_input09(self):
        """
        Compare test input to provided true answer
        """
        testData = ')())())'
        result = calculate(testData)
        self.assertEqual(result, -3)


if __name__ == '__main__':
    unittest.main()

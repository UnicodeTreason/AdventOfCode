import unittest

from solutions.year2015.day1 import calculate


class TestSum(unittest.TestCase):

    def test_year2015_day1_input1(self):
        """
        Compare test input to provided true answer
        """
        testData = '(())'
        result = calculate(testData)
        self.assertEqual(result, 0)

    def test_year2015_day1_input2(self):
        """
        Compare test input to provided true answer
        """
        testData = '()()'
        result = calculate(testData)
        self.assertEqual(result, 0)

    def test_year2015_day1_input3(self):
        """
        Compare test input to provided true answer
        """
        testData = '((('
        result = calculate(testData)
        self.assertEqual(result, 3)

    def test_year2015_day1_input4(self):
        """
        Compare test input to provided true answer
        """
        testData = '(()(()('
        result = calculate(testData)
        self.assertEqual(result, 3)

    def test_year2015_day1_input5(self):
        """
        Compare test input to provided true answer
        """
        testData = '))((((('
        result = calculate(testData)
        self.assertEqual(result, 3)

    def test_year2015_day1_input6(self):
        """
        Compare test input to provided true answer
        """
        testData = '())'
        result = calculate(testData)
        self.assertEqual(result, -1)

    def test_year2015_day1_input7(self):
        """
        Compare test input to provided true answer
        """
        testData = '))('
        result = calculate(testData)
        self.assertEqual(result, -1)

    def test_year2015_day1_input8(self):
        """
        Compare test input to provided true answer
        """
        testData = ')))'
        result = calculate(testData)
        self.assertEqual(result, -3)

    def test_year2015_day1_input9(self):
        """
        Compare test input to provided true answer
        """
        testData = ')())())'
        result = calculate(testData)
        self.assertEqual(result, -3)


if __name__ == '__main__':
    unittest.main()

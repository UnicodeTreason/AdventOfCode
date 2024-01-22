import unittest

from solutions.year2015.day06 import calculate


class TestSum(unittest.TestCase):

    def test_year2015_day06_input01(self):
        """
        Compare test input to provided true answer
        """
        testData = ['turn on 0,0 through 2,2']
        result = calculate(testData)
        self.assertEqual(result, 9)

    def test_year2015_day06_input02(self):
        """
        Compare test input to provided true answer
        """
        testData = ['turn on 0,0 through 999,999']
        result = calculate(testData)
        self.assertEqual(result, 1000000)

    def test_year2015_day06_input03(self):
        """
        Compare test input to provided true answer
        """
        testData = ['turn on 0,0 through 999,999', 'turn off 499,499 through 500,500']
        result = calculate(testData)
        self.assertEqual(result, 999996)

    def test_year2015_day06_input04(self):
        """
        Compare test input to provided true answer
        """
        testData = ['turn on 0,0 through 999,999', 'toggle 499,499 through 500,500']
        result = calculate(testData)
        self.assertEqual(result, 999996)

    def test_year2015_day06_input05(self):
        """
        Compare test input to provided true answer
        """
        testData = ['toggle 0,0 through 999,0']
        result = calculate(testData)
        self.assertEqual(result, 1000)

    def test_year2015_day06_input06(self):
        """
        Compare test input to provided true answer
        """
        testData = ['toggle 0,0 through 0,999']
        result = calculate(testData)
        self.assertEqual(result, 1000)

    def test_year2015_day06_input07(self):
        """
        Compare test input to provided true answer
        """
        testData = ['turn on 0,0 through 0,0']
        result = calculate(testData, True)
        self.assertEqual(result, 1)

    def test_year2015_day06_input08(self):
        """
        Compare test input to provided true answer
        """
        testData = ['toggle 0,0 through 999,999']
        result = calculate(testData, True)
        self.assertEqual(result, 2000000)


if __name__ == '__main__':
    unittest.main()

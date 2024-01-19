import unittest

from solutions.year2015.day05 import calculate


class TestSum(unittest.TestCase):

    def test_year2015_day05_input01(self):
        """
        Compare test input to provided true answer
        """
        testData = ['ugknbfddgicrmopn']
        result = calculate(testData)
        self.assertEqual(result, 1)

    def test_year2015_day05_input02(self):
        """
        Compare test input to provided true answer
        """
        testData = ['aaa']
        result = calculate(testData)
        self.assertEqual(result, 1)

    def test_year2015_day05_input03(self):
        """
        Compare test input to provided true answer
        """
        testData = ['jchzalrnumimnmhp']
        result = calculate(testData)
        self.assertEqual(result, 0)

    def test_year2015_day05_input04(self):
        """
        Compare test input to provided true answer
        """
        testData = ['haegwjzuvuyypxyu']
        result = calculate(testData)
        self.assertEqual(result, 0)

    def test_year2015_day05_input05(self):
        """
        Compare test input to provided true answer
        """
        testData = ['dvszwmarrgswjxmb']
        result = calculate(testData)
        self.assertEqual(result, 0)

    def test_year2015_day05_input06(self):
        """
        Compare test input to provided true answer
        """
        testData = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
        result = calculate(testData)
        self.assertEqual(result, 2)

    def test_year2015_day05_input07(self):
        """
        Compare test input to provided true answer
        """
        testData = ['xyxy']
        result = calculate(testData, True)
        self.assertEqual(result, 1)

    def test_year2015_day05_input08(self):
        """
        Compare test input to provided true answer
        """
        testData = ['qjhvhtzxzqqjkmpb']
        result = calculate(testData, True)
        self.assertEqual(result, 1)

    def test_year2015_day05_input09(self):
        """
        Compare test input to provided true answer
        """
        testData = ['xxyxx']
        result = calculate(testData, True)
        self.assertEqual(result, 1)

    def test_year2015_day05_input10(self):
        """
        Compare test input to provided true answer
        """
        testData = ['uurcxstgmygtbstg']
        result = calculate(testData, True)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()

import unittest

from adventofcode.year2015.day07 import calculate


class TestSum(unittest.TestCase):

    def test_year2015_day07_input01(self):
        """
        Compare test input to provided true answer
        """
        testData = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> i']
        result = calculate(testData)
        self.assertEqual(result, {'d': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456})

    def test_year2015_day07_input02(self):
        """
        Compare test input to provided true answer
        """
        testData = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'y -> z', 'NOT x -> h', 'NOT y -> i']
        result = calculate(testData)
        self.assertEqual(result, {'d': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456, 'z': 456})

    def test_year2015_day07_input03(self):
        """
        Compare test input to provided true answer
        """
        testData = ['a AND b -> c', '1 -> a', '2 -> b']
        result = calculate(testData)
        self.assertEqual(result, {'a': 1, 'b': 2, 'c': 0})

    def test_year2015_day07_input04(self):
        """
        Compare test input to provided true answer
        """
        testData = ['a AND b -> c', '1 -> a', '2 -> b']
        result = calculate(testData, True)
        self.assertEqual(result, {'a': 1, 'b': 46065, 'c': 1})


if __name__ == '__main__':
    unittest.main()

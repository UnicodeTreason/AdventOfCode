import pytest
import unittest

from adventofcode.year2015.day01 import part_one, part_two


# Trying out pytest
@pytest.mark.parametrize('test_input, expected', [
    ('(())', 0),
    ('()()', 0),
    ('(((', 3),
    ('(()(()(', 3),
    ('))(((((', 3),
    ('())', -1),
    ('))(', -1),
    (')))', -3),
])
def test_part_one(test_input, expected):
    assert part_one(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    (')())())', 1),
    ('(()))', 5),
])
def test_part_two(test_input, expected):
    assert part_two(test_input) == expected


class TestSum(unittest.TestCase):

    def test_year2015_day01_part_one_test01(self):
        testData = '(())'
        result = part_one(testData)
        self.assertEqual(result, 0)

    def test_year2015_day01_part_one_test02(self):
        testData = '()()'
        result = part_one(testData)
        self.assertEqual(result, 0)

    def test_year2015_day01_part_one_test03(self):
        testData = '((('
        result = part_one(testData)
        self.assertEqual(result, 3)

    def test_year2015_day01_part_one_test04(self):
        testData = '(()(()('
        result = part_one(testData)
        self.assertEqual(result, 3)

    def test_year2015_day01_part_one_test05(self):
        testData = '))((((('
        result = part_one(testData)
        self.assertEqual(result, 3)

    def test_year2015_day01_part_one_test06(self):
        testData = '())'
        result = part_one(testData)
        self.assertEqual(result, -1)

    def test_year2015_day01_part_one_test07(self):
        testData = '))('
        result = part_one(testData)
        self.assertEqual(result, -1)

    def test_year2015_day01_part_one_test08(self):
        testData = ')))'
        result = part_one(testData)
        self.assertEqual(result, -3)

    def test_year2015_day01_part_one_test09(self):
        testData = ')())())'
        result = part_one(testData)
        self.assertEqual(result, -3)

    def test_year2015_day01_part_two_test01(self):
        testData = ')())())'
        result = part_two(testData)
        self.assertEqual(result, 1)

    def test_year2015_day01_part_two_test02(self):
        testData = '(()))'
        result = part_two(testData)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()

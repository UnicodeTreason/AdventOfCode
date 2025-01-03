import pytest

from adventofcode.year2015.day08 import part_one, part_two


@pytest.mark.parametrize('test_input, expected', [
    ([r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'], 12),
])
def test_part_one(test_input, expected):
    assert part_one(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ([r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'], 19),
])
def test_part_two(test_input, expected):
    assert part_two(test_input) == expected

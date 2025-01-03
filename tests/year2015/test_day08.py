import pytest

from adventofcode.year2015.day08 import part_one


@pytest.mark.parametrize('test_input, expected', [
    ([r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'], 12),
])
def test_part_one(test_input, expected):
    assert part_one(test_input) == expected

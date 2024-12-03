import pytest

from adventofcode.year2024.day01 import part_one, part_two


@pytest.mark.parametrize('test_input, expected', [
    (['3   4', '4   3', '2   5', '1   3', '3   9', '3   3'], 11),
])
def test_part_one(test_input, expected):
    assert part_one(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    (['3   4', '4   3', '2   5', '1   3', '3   9', '3   3'], 31),
])
def test_part_two(test_input, expected):
    assert part_two(test_input) == expected

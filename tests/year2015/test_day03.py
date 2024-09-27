import pytest

from adventofcode.year2015.day03 import part_one, part_two


@pytest.mark.parametrize('test_input, expected', [
    ('>', 2),
    ('^>v<', 4),
    ('^v^v^v^v^v', 2),
])
def test_part_one(test_input, expected):
    assert part_one(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('^v', 3),
    ('^>v<', 3),
    ('^v^v^v^v^v', 11),
])
def test_part_two(test_input, expected):
    assert part_two(test_input) == expected

import pytest

from adventofcode.year2015.day02 import part_one, part_two


@pytest.mark.parametrize('test_input, expected', [
    (['2x3x4'], 58),
    (['1x1x10'], 43),
    (['2x3x4', '1x1x10'], 101),
])
def test_part_one(test_input, expected):
    assert part_one(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    (['2x3x4'], 34),
    (['1x1x10'], 14),
    (['2x3x4', '1x1x10'], 48),
])
def test_part_two(test_input, expected):
    assert part_two(test_input) == expected

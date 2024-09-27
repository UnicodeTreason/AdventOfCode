import pytest

from adventofcode.year2015.day06 import part_one, part_two


@pytest.mark.parametrize('test_input, expected', [
    (['turn on 0,0 through 2,2'], 9),
    (['turn on 0,0 through 999,999'], 1000000),
    (['turn on 0,0 through 999,999', 'turn off 499,499 through 500,500'], 999996),
    (['turn on 0,0 through 999,999', 'toggle 499,499 through 500,500'], 999996),
    (['toggle 0,0 through 999,0'], 1000),
    (['toggle 0,0 through 0,999'], 1000),
])
def test_part_one(test_input, expected):
    assert part_one(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    (['turn on 0,0 through 0,0'], 1),
    (['toggle 0,0 through 999,999'], 2000000),
])
def test_part_two(test_input, expected):
    assert part_two(test_input) == expected

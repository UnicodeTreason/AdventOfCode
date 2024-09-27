import pytest

from adventofcode.year2015.day05 import part_one, part_two


@pytest.mark.parametrize('test_input, expected', [
    (['ugknbfddgicrmopn'], 1),
    (['aaa'], 1),
    (['jchzalrnumimnmhp'], 0),
    (['haegwjzuvuyypxyu'], 0),
    (['dvszwmarrgswjxmb'], 0),
    (['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb'], 2),
])
def test_part_one(test_input, expected):
    assert part_one(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    (['xyxy'], 1),
    (['qjhvhtzxzqqjkmpb'], 1),
    (['xxyxx'], 1),
    (['uurcxstgmygtbstg'], 0),
])
def test_part_two(test_input, expected):
    assert part_two(test_input) == expected

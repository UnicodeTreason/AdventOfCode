import pytest

from adventofcode.year2015.day04 import part_one, part_two


@pytest.mark.parametrize('test_input, expected', [
    ('abcdef', 609043),
    ('pqrstuv', 1048970),
])
def test_part_one(test_input, expected):
    assert part_one(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('yzbqklnj', 9962624),
])
def test_part_two(test_input, expected):
    assert part_two(test_input) == expected

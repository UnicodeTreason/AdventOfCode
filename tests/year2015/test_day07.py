import pytest

from adventofcode.year2015.day07 import part_one, part_two


@pytest.mark.parametrize('test_input, expected', [
    (['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> i'], {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456
    }),
    (['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'y -> z', 'NOT x -> h', 'NOT y -> i'], {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456,
        'z': 456
    }),
    (['a AND b -> c', '1 -> a', '2 -> b'], {
        'a': 1,
        'b': 2,
        'c': 0
    }),
])
def test_part_one(test_input, expected):
    assert part_one(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [
    (['a AND b -> c', '1 -> a', '2 -> b'], {
        'a': 1,
        'b': 46065,
        'c': 1
    }),
])
def test_part_two(test_input, expected):
    assert part_two(test_input) == expected

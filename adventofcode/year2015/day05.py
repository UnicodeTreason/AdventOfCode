from pathlib import Path
import re


# --- Day 5: Doesn't He Have Intern-Elves For This? ---
def part_one(input_data: list) -> int:
    """Calculate count of nice strings

    Parameters
    ----------
    input_data: list
        The list of all strings to check
            ugknbfddgicrmopn

    Returns
    -------
    output_nice_strings: int
    """
    output_nice_strings = 0

    # Check for Nice
    # >= 3 Vowels
    # >= 1 pair of letters
    # not contain ab, cd, pq, xy
    nice_checks = [{'name': 'Vowels', 'regex': r'([aeiou].*){3,}'}, {'name': 'LetterPairs', 'regex': r'([a-z])\1'}, {'name': 'BannedStrings', 'regex': r'(ab|cd|pq|xy)'}]

    for string in input_data:
        naughty = False
        for check in nice_checks:
            # Perform required regex checks
            match check['name']:
                case 'BannedStrings':
                    match = re.findall(check['regex'], string)
                    if len(match) > 0:
                        naughty = True  # Naughty string
                case _:
                    if not re.search(check['regex'], string):
                        naughty = True  # Naughty string

        # Skip to next string
        if naughty:
            continue

        # If we made it here, string must be Nice
        output_nice_strings += 1

    return output_nice_strings


def part_two(input_data: list) -> int:
    """Calculate count of nice strings

    Parameters
    ----------
    input_data: list
        The list of all strings to check
            ugknbfddgicrmopn

    Returns
    -------
    output_nice_strings: int
    """
    output_nice_strings = 0

    # Check for Nice
    # >= 1 pair of letters
    nice_checks = [{'name': 'LetterPairs', 'regex': r'([a-z][a-z]).*\1'}, {'name': 'LetterRepeat', 'regex': r'([a-z]).\1'}]

    for string in input_data:
        naughty = False
        for check in nice_checks:
            # Perform required regex checks
            match check['name']:
                case 'BannedStrings':
                    match = re.findall(check['regex'], string)
                    if len(match) > 0:
                        naughty = True  # Naughty string
                case _:
                    if not re.search(check['regex'], string):
                        naughty = True  # Naughty string

        # Skip to next string
        if naughty:
            continue

        # If we made it here, string must be Nice
        output_nice_strings += 1

    return output_nice_strings


if __name__ == "__main__":
    # Read input from disk cache
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'

    # Parse input into usable format
    with path_inputs.open('r') as f:
        input_data = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Part 01: {part_one(input_data)}')
    print(f'Part 02: {part_two(input_data)}')

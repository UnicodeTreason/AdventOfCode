from pathlib import Path
import re


def calculate(inputData: list, magic: bool = False) -> int:
    """Calculate count of nice strings"

    Parameters
    ----------
    inputData : list
        The list of all strings to check
            ugknbfddgicrmopn
    magic : bool, optional
        A flag used to print the Part 2 output

    Returns
    -------
    int
        magic: False
            The count of strings that are nice ruleset#1
        magic: True
            The count of strings that are nice ruleset#2
    """
    outputNiceStrings = 0

    # Part 2 Switch
    if magic:
        # Check for Nice
        # >= 1 pair of letters
        niceChecks = [{
            'name': 'LetterPairs',
            'regex': r'([a-z][a-z]).*\1'
        }, {
            'name': 'LetterRepeat',
            'regex': r'([a-z]).\1'
        }]
    else:
        # Check for Nice
        # >= 3 Vowels
        # >= 1 pair of letters
        # not contain ab, cd, pq, xy
        niceChecks = [{
            'name': 'Vowels',
            'regex': r'([aeiou].*){3,}'
        }, {
            'name': 'LetterPairs',
            'regex': r'([a-z])\1'
        }, {
            'name': 'BannedStrings',
            'regex': r'(ab|cd|pq|xy)'
        }]

    for string in inputData:
        naughty = False
        for check in niceChecks:
            # print(f'Match: {match}')
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
        outputNiceStrings += 1

    return outputNiceStrings


if __name__ == "__main__":
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'
    with path_inputs.open('r') as f:
        inputData = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(inputData)}')
    print(f'Solution 02: {calculate(inputData,True)}')

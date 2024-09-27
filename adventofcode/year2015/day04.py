from pathlib import Path
import hashlib
import re


# --- Day 4: The Ideal Stocking Stuffer ---
def part_one(input_data: str) -> int:
    """Calculate a valid mined hash for AdventCoin
    A mined hash is the lowest number that combines with the secret key to produce output starting with 5 zeroes

    Parameters
    ----------
    input_data: str
        The str based secret key for mining
            abcdef

    Returns
    -------
    output_mine_number: int
    """
    output_mine_number = 0
    hash_valid = False

    while not hash_valid:
        # Munge secret key and current number together
        hash_key = str(input_data) + str(output_mine_number)
        hash_MD5 = hashlib.md5(hash_key.encode('utf-8')).hexdigest()

        regex_count = '0{5}.+'

        if re.match(regex_count, hash_MD5):
            hash_valid = True
        else:
            output_mine_number += 1

    return output_mine_number


def part_two(input_data: str) -> int:
    """Calculate a valid mined hash for AdventCoin
    A mined hash is the lowest number that combines with the secret key to produce output starting with 6 zeroes

    Parameters
    ----------
    input_data: str
        The str based secret key for mining
            abcdef

    Returns
    -------
    output_mine_number: int
    """
    output_mine_number = 0
    hash_valid = False

    while not hash_valid:
        # Munge secret key and current number together
        hash_key = str(input_data) + str(output_mine_number)
        hash_MD5 = hashlib.md5(hash_key.encode('utf-8')).hexdigest()

        regex_count = '0{6}.+'

        if re.match(regex_count, hash_MD5):
            hash_valid = True
        else:
            output_mine_number += 1

    return output_mine_number


if __name__ == "__main__":
    # Read input from disk cache
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'

    # Parse input into usable format
    with path_inputs.open('r') as f:
        input_data = f.read()

    print('Calculating Solutions...')
    print(f'Part 01: {part_one(input_data)}')
    print(f'Part 02: {part_two(input_data)}')

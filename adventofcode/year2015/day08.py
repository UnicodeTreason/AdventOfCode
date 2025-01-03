import re
from pathlib import Path


# --- Day 8: Matchsticks ---
def part_one(input_data: list) -> dict:
    """Calculate

    Parameters
    ----------
    input_data: list
        List of strings containing the following elements:
            double-quoted string literals: "abc"
            escape sequences:
                \\ (which represents a single backslash)
                \" (which represents a lone double-quote character)
                \ x plus two hexadecimal characters (which represents a single character with that ASCII code)

    Returns
    -------
    characters_code - characters_memory: int
    """

    characters_code = 0
    characters_memory = 0

    # Process Input
    for escaped_string in input_data:
        # Count of characters at the code level
        print(f'STR: {escaped_string}')
        print(f'LEN: {len(escaped_string)}')
        characters_code += len(escaped_string)

        # Count of characters at the memory level
        # Drop outside quotes
        escaped_string = escaped_string.rstrip(r'"')
        escaped_string = escaped_string.lstrip(r'"')
        # Replace escaped quote with quote
        escaped_string = escaped_string.replace(r'\"', '"')
        # Replace escaped hexadecimal with a single char
        escaped_string = re.sub(r'\\x([0-9]|[a-f]){2}', 'X', escaped_string)
        # Replace escaped backslash with backslash
        escaped_string = escaped_string.replace(r'\\', '\\')
        characters_memory += len(escaped_string)
        print(f'STR: {escaped_string}')
        print(f'LEN: {len(escaped_string)}')
        print('')

    print(f'code: {characters_code}')
    print(f'memory: {characters_memory}')
    return characters_code - characters_memory


if __name__ == "__main__":
    # Read input from disk cache
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'

    # Parse input into usable format
    with path_inputs.open('r') as f:
        input_data = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Part 01: {part_one(input_data)}')
    # print(f'Part 02: {part_two(input_data)}')

import re
from pathlib import Path


# --- Day 8: Matchsticks ---
def part_one(input_data: list) -> int:
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
        # Add count
        characters_memory += len(escaped_string)
    return characters_code - characters_memory


def part_two(input_data: list) -> int:
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
    characters_recoded - characters_code: int
    """

    characters_recoded = 0
    characters_code = 0

    # Process Input
    for escaped_string in input_data:
        # Count of characters at the code level
        characters_code += len(escaped_string)

        # Count of characters after recoding
        # Replace backslash with escaped backslash
        escaped_string = escaped_string.replace('\\', r'\\')
        # Replace quote with escaped quote
        escaped_string = escaped_string.replace(r'"', r'\"')
        # Add outside quotes
        escaped_string = '"' + escaped_string + '"'
        # Add count
        characters_recoded += len(escaped_string)
    return characters_recoded - characters_code


if __name__ == "__main__":
    # Read input from disk cache
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'

    # Parse input into usable format
    with path_inputs.open('r') as f:
        input_data = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Part 01: {part_one(input_data)}')
    print(f'Part 02: {part_two(input_data)}')

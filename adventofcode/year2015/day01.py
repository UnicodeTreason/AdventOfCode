from pathlib import Path


# --- Day 1: Not Quite Lisp ---
def part_one(input_data: str) -> int:
    """Calculate final floor Santa ends up on.

    Parameters
    ----------
    input_data: str
        The string of characters acting as a map of staircase instructions
            ( = Up a floor
            ) = Down a floor

    Returns
    -------
    current_floor: int
    """
    current_floor = 0

    # Process every instruction
    for index, char in enumerate(input_data):
        if char == '(':
            current_floor += 1
        elif char == ')':
            current_floor -= 1
    return current_floor


def part_two(input_data: str) -> int:
    """Calculate index of instruction where Santa finds the basement for the first time

    Parameters
    ----------
    input_data: str
        The string of characters acting as a map of staircase instructions
            ( = Up a floor
            ) = Down a floor

    Returns
    -------
    index: int
    """
    current_floor = 0

    # Process every instruction
    for index, char in enumerate(input_data):
        if char == '(':
            current_floor += 1
        elif char == ')':
            current_floor -= 1

        # Calculate position in data when basement first seen
        if current_floor <= -1:
            # Add 1 to account for arrays starting at 0
            return index + 1


if __name__ == "__main__":
    # Read input from disk cache
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'

    # Parse input into usable format
    with path_inputs.open('r') as f:
        input_data = f.read()

    print('Calculating Solutions...')
    print(f'Part 01: {part_one(input_data)}')
    print(f'Part 02: {part_two(input_data)}')

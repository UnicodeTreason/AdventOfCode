from pathlib import Path


# --- Day 1: Historian Hysteria ---
def part_one(input_data: str) -> int:
    """Calculate absolute difference between two lists of IDs.

    Parameters
    ----------
    input_data: list
        A list containing all lines of input ready for splitting into two sub lists

    Returns
    -------
    sum(calculated_distances): int
    """
    left_list = []
    right_list = []
    calculated_distances = []

    # Process initial list into two lists
    for line in input_data:
        left_value, right_value = line.split()
        left_list.append(int(left_value))
        right_list.append(int(right_value))

    # Sort lists min->max
    left_list.sort()
    right_list.sort()

    # Process lists
    for left_list_value in left_list.copy():
        # Absolute value of left - right
        calculated_distances.append(abs(int(right_list.pop(0)) - int(left_list.pop(0))))
    return sum(calculated_distances)


def part_two(input_data: str) -> int:
    """Calculate similarity score between two lists of IDs.

    Parameters
    ----------
    input_data: list
        A list containing all lines of input ready for splitting into two sub lists

    Returns
    -------
    sum(similarity_scores): int
    """
    left_list = []
    right_list = []
    similarity_scores = []

    # Process initial list into two lists
    for line in input_data:
        left_value, right_value = line.split()
        left_list.append(int(left_value))
        right_list.append(int(right_value))

    # Calculate similarity scores
    for left_list_value in left_list:
        similarity_scores.append(left_list_value * right_list.count(left_list_value))
    return sum(similarity_scores)


if __name__ == "__main__":
    # Read input from disk cache
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'

    # Parse input into usable format
    with path_inputs.open('r') as f:
        input_data = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Part 01: {part_one(input_data)}')
    print(f'Part 02: {part_two(input_data)}')

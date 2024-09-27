from pathlib import Path


# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
def part_one(input_data: str) -> int:
    """Calculate count houses that recieve atleast one present

    Parameters
    ----------
    input_data: str
        The str of moves to make
            ^v^v^v^v^v

    Returns
    -------
    len(output_houses_delivered): int
    """
    output_houses_delivered = ['[0, 0]']
    location_santa = [0, 0]

    # Calculate moves and outcome
    for move in input_data:
        if move == '>':
            location_santa[1] += 1
        elif move == '<':
            location_santa[1] -= 1
        elif move == '^':
            location_santa[0] += 1
        elif move == 'v':
            location_santa[0] -= 1

        # Track visited locations
        if f'{location_santa}' not in output_houses_delivered:
            output_houses_delivered.append(f'{location_santa}')

    return len(output_houses_delivered)


def part_two(input_data: str) -> int:
    """Calculate count houses that recieve atleast one present

    Parameters
    ----------
    input_data: str
        The str of moves to make
            ^v^v^v^v^v

    Returns
    -------
    len(output_houses_delivered): int
    """
    output_houses_delivered = ['[0, 0]']
    location_santa = [0, 0]
    location_zanta = [0, 0]
    turn_tracker = 'S'

    for move in input_data:
        # Calculate Move and outcome
        if move == '>':
            if turn_tracker == 'S':
                location_santa[1] += 1
            elif turn_tracker == 'Z':
                location_zanta[1] += 1
        elif move == '<':
            if turn_tracker == 'S':
                location_santa[1] -= 1
            elif turn_tracker == 'Z':
                location_zanta[1] -= 1
        elif move == '^':
            if turn_tracker == 'S':
                location_santa[0] += 1
            elif turn_tracker == 'Z':
                location_zanta[0] += 1
        elif move == 'v':
            if turn_tracker == 'S':
                location_santa[0] -= 1
            elif turn_tracker == 'Z':
                location_zanta[0] -= 1

        # Track visited locations
        if turn_tracker == 'S':
            if f'{location_santa}' not in output_houses_delivered:
                output_houses_delivered.append(f'{location_santa}')
        elif turn_tracker == 'Z':
            if f'{location_zanta}' not in output_houses_delivered:
                output_houses_delivered.append(f'{location_zanta}')

        # Swap to next "Santa"
        if turn_tracker == 'S':
            turn_tracker = 'Z'
        elif turn_tracker == 'Z':
            turn_tracker = 'S'

    return len(output_houses_delivered)


if __name__ == "__main__":
    # Read input from disk cache
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'

    # Parse input into usable format
    with path_inputs.open('r') as f:
        input_data = f.read()

    print('Calculating Solutions...')
    print(f'Part 01: {part_one(input_data)}')
    print(f'Part 02: {part_two(input_data)}')

from pathlib import Path


def calculate(inputData: str, magic: bool = False) -> int:
    """Calculate square footage of wrapping paper for a package using formula "2*l*w + 2*w*h + 2*h*l"

    Parameters
    ----------
    inputData : str
        The str of moves to make
            ^v^v^v^v^v
    magic : bool, optional
        A flag used to print the Part 2 output

    Returns
    -------
    int
        magic: False
            The count of houses with >= 1 present
        magic: True
            The count of houses with >= 1 present after being visited by both Santas
    """
    outputHousesDelivered = ['[0, 0]']
    locationSanta = [0, 0]
    locationZanta = [0, 0]
    turnTracker = 'S'

    for move in inputData:
        # Calculate Move and outcome
        if move == '>':
            if turnTracker == 'S':
                locationSanta[1] += 1
            elif turnTracker == 'Z':
                locationZanta[1] += 1
        elif move == '<':
            if turnTracker == 'S':
                locationSanta[1] -= 1
            elif turnTracker == 'Z':
                locationZanta[1] -= 1
        elif move == '^':
            if turnTracker == 'S':
                locationSanta[0] += 1
            elif turnTracker == 'Z':
                locationZanta[0] += 1
        elif move == 'v':
            if turnTracker == 'S':
                locationSanta[0] -= 1
            elif turnTracker == 'Z':
                locationZanta[0] -= 1

        # Track visited locations
        if turnTracker == 'S':
            if f'{locationSanta}' not in outputHousesDelivered:
                outputHousesDelivered.append(f'{locationSanta}')
        elif turnTracker == 'Z':
            if f'{locationZanta}' not in outputHousesDelivered:
                outputHousesDelivered.append(f'{locationZanta}')

        # Part 2 Switch
        # Flip/Flop the turn tracker
        if magic:
            if turnTracker == 'S':
                turnTracker = 'Z'
            elif turnTracker == 'Z':
                turnTracker = 'S'

    return len(outputHousesDelivered)


if __name__ == "__main__":
    path_inputs = Path(__file__).parent / 'inputs' / 'day3_input.txt'
    with path_inputs.open('r') as f:
        inputData = f.read()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(inputData)}')
    print(f'Solution 02: {calculate(inputData,True)}')

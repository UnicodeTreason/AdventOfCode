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
            The something
    """
    outputHousesDelivered = ['[0, 0]']
    calculatedLocation = [0,0]

    for move in inputData:
        # Calculate Move and outcome
        if move == '>':
            calculatedLocation[1] += 1
        elif move == '<':
            calculatedLocation[1] -= 1
        elif move == '^':
            calculatedLocation[0] += 1
        elif move == 'v':
            calculatedLocation[0] -= 1

        # Track visited locations
        if f'{calculatedLocation}' not in outputHousesDelivered:
            outputHousesDelivered.append(f'{calculatedLocation}')

        # Part 2 Switch
        # Calculate
        if magic:
            pass

    return len(outputHousesDelivered)


if __name__ == "__main__":
    p = Path(__file__).with_name('day3_input.txt')
    with p.open('r') as f:
        inputData = f.read()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(inputData)}')
    print(f'Solution 02: {calculate(inputData,True)}')

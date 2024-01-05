from pathlib import Path


def calculate(inputData: str, magic: bool = False) -> int:
    """Calculate desired floor from input map

    Parameters
    ----------
    inputData : str
        The string of characters acting as a map of staircase instructions
            ( = Up a floor
            ) = Down a floor
    magic : bool, optional
        A flag used to print the Part 2 output

    Returns
    -------
    int
        magic: False
            The final floor
        magic: True
            The position of the instruction when the basement is seen for the first time
    """
    output = 0

    for index, char in enumerate(inputData):
        # Perform the calculation
        if char == '(':
            output += 1
        elif char == ')':
            output -= 1

        # Part 2 Switch
        # Calculate position in data when basement first seen
        if magic:
            if output <= -1:
                # Add 1 to account for arrays starting at 0
                return index + 1
    return output


if __name__ == "__main__":
    path_inputs = Path(__file__).parent / 'inputs' / 'day1_input.txt'
    with path_inputs.open('r') as f:
        inputData = f.read()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(inputData)}')
    print(f'Solution 02: {calculate(inputData,True)}')

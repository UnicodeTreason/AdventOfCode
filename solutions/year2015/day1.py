from pathlib import Path


def calculate(inputData, magic=False):
    # ( means go up a floor
    # ) means go down a floor
    outputFloor = 0

    for index, char in enumerate(inputData):
        if char == '(':
            outputFloor += 1
        elif char == ')':
            outputFloor -= 1

        # Part 2 Switch
        # Calculate position in data when basement first seen
        if magic:
            if outputFloor <= -1:
                # Add 1 to account for arrays starting at 0
                return index + 1
    return outputFloor


if __name__ == "__main__":
    p = Path(__file__).with_name('day1_input.txt')
    with p.open('r') as f:
        inputData = f.read()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(inputData)}')
    print(f'Solution 02: {calculate(inputData,True)}')

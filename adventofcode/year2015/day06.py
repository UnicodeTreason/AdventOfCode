from pathlib import Path
from collections import defaultdict
import re


def calculate(input_data: list, magic: bool = False) -> int:
    """Calculate 2D array of lights"

    Parameters
    ----------
    input_data: list
        List of strings containing the following elements:
            powerStatus:
                turn off
                turn on
                toggle
            co-ords range of lights: 0,0 through 999,999
    magic: bool, optional
        A flag used to print the Part 2 output

    Returns
    -------
    int
        magic: False
            The count of lights powered on.
        magic: True
            The brightness of all lights.
    """

    # Initialise dict
    rowMax = 1000
    colMax = 1000
    gridLights = defaultdict(dict)  # Using this allows Python to generate dict keys on first access
    outputLightsOn = 0

    # Initialise the grid
    for row in range(0, rowMax):
        for col in range(0, colMax):
            gridLights[row][col] = 0

    # Perform desired commands on grid
    for command in input_data:
        cmdParts = re.match(r'^(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)$', command)
        cmdPower = cmdParts.group(1)
        cmdStartLoc = cmdParts.group(2)
        cmdStartRow = int(cmdStartLoc.split(',')[0])
        cmdStartCol = int(cmdStartLoc.split(',')[1])
        cmdEndLoc = cmdParts.group(3)
        cmdEndRow = int(cmdEndLoc.split(',')[0]) + 1
        cmdEndCol = int(cmdEndLoc.split(',')[1]) + 1

        # Iterate over the grid
        for row in range(cmdStartRow, cmdEndRow):
            for col in range(cmdStartCol, cmdEndCol):
                if magic:
                    match cmdPower:
                        case 'turn on':
                            gridLights[row][col] += 1
                        case 'turn off':
                            if gridLights[row][col] >= 1:
                                gridLights[row][col] -= 1
                        case 'toggle':
                            gridLights[row][col] += 2
                else:
                    match cmdPower:
                        case 'turn on':
                            gridLights[row][col] = 1
                        case 'turn off':
                            gridLights[row][col] = 0
                        case 'toggle':
                            if gridLights[row][col] == 1:
                                gridLights[row][col] = 0
                            else:
                                gridLights[row][col] = 1

    # Count the grid
    for row in range(0, rowMax):
        for col in range(0, colMax):
            outputLightsOn += gridLights[row][col]

    return outputLightsOn


if __name__ == "__main__":
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'
    with path_inputs.open('r') as f:
        input_data = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(input_data)}')
    print(f'Solution 02: {calculate(input_data,True)}')

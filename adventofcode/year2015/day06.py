from pathlib import Path
from collections import defaultdict
import re


# --- Day 6: Probably a Fire Hazard ---
def part_one(input_data: list) -> int:
    """Calculate 2D array of lights that are powered on

    Parameters
    ----------
    input_data: list
        List of strings containing the following elements:
            powerStatus:
                turn off
                turn on
                toggle
            co-ords range of lights: 0,0 through 999,999

    Returns
    -------
    output_lights_on: int
            The brightness of all lights.
    """

    # Initialise dict
    row_max = 1000
    col_max = 1000
    grid_lights = defaultdict(dict)  # Using this allows Python to generate dict keys on first access
    output_lights_on = 0

    # Initialise the grid
    for row in range(0, row_max):
        for col in range(0, col_max):
            grid_lights[row][col] = 0

    # Perform desired commands on grid
    for command in input_data:
        cmd_parts = re.match(r'^(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)$', command)
        cmd_power = cmd_parts.group(1)
        cmd_start_loc = cmd_parts.group(2)
        cmd_start_row = int(cmd_start_loc.split(',')[0])
        cmd_start_col = int(cmd_start_loc.split(',')[1])
        cmd_end_loc = cmd_parts.group(3)
        cmd_end_row = int(cmd_end_loc.split(',')[0]) + 1
        cmd_end_col = int(cmd_end_loc.split(',')[1]) + 1

        # Iterate over the grid
        for row in range(cmd_start_row, cmd_end_row):
            for col in range(cmd_start_col, cmd_end_col):
                match cmd_power:
                    case 'turn on':
                        grid_lights[row][col] = 1
                    case 'turn off':
                        grid_lights[row][col] = 0
                    case 'toggle':
                        if grid_lights[row][col] == 1:
                            grid_lights[row][col] = 0
                        else:
                            grid_lights[row][col] = 1

    # Count the grid
    for row in range(0, row_max):
        for col in range(0, col_max):
            output_lights_on += grid_lights[row][col]

    return output_lights_on


def part_two(input_data: list) -> int:
    """Calculate 2D array of lights and their brightness

    Parameters
    ----------
    input_data: list
        List of strings containing the following elements:
            powerStatus:
                turn off (decrease brightness)
                turn on (increase brightness)
                toggle (increase brightness by 2)
            co-ords range of lights: 0,0 through 999,999
    magic: bool, optional
        A flag used to print the Part 2 output

    Returns
    -------
    output_lights_brightness: int
    """

    # Initialise dict
    row_max = 1000
    col_max = 1000
    grid_lights = defaultdict(dict)  # Using this allows Python to generate dict keys on first access
    output_lights_brightness = 0

    # Initialise the grid
    for row in range(0, row_max):
        for col in range(0, col_max):
            grid_lights[row][col] = 0

    # Perform desired commands on grid
    for command in input_data:
        cmd_parts = re.match(r'^(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)$', command)
        cmd_power = cmd_parts.group(1)
        cmd_start_loc = cmd_parts.group(2)
        cmd_start_row = int(cmd_start_loc.split(',')[0])
        cmd_start_col = int(cmd_start_loc.split(',')[1])
        cmd_end_loc = cmd_parts.group(3)
        cmd_end_row = int(cmd_end_loc.split(',')[0]) + 1
        cmd_end_col = int(cmd_end_loc.split(',')[1]) + 1

        # Iterate over the grid
        for row in range(cmd_start_row, cmd_end_row):
            for col in range(cmd_start_col, cmd_end_col):
                match cmd_power:
                    case 'turn on':
                        grid_lights[row][col] += 1
                    case 'turn off':
                        if grid_lights[row][col] >= 1:
                            grid_lights[row][col] -= 1
                    case 'toggle':
                        grid_lights[row][col] += 2

    # Count the grid
    for row in range(0, row_max):
        for col in range(0, col_max):
            output_lights_brightness += grid_lights[row][col]

    return output_lights_brightness


if __name__ == "__main__":
    # Read input from disk cache
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'

    # Parse input into usable format
    with path_inputs.open('r') as f:
        input_data = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Part 01: {part_one(input_data)}')
    print(f'Part 02: {part_two(input_data)}')

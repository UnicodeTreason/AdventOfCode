from pathlib import Path


# --- Day 2: I Was Told There Would Be No Math ---
def part_one(input_data: list) -> int:
    """Calculate square footage of wrapping paper for all packages

    Formula: "2*l*w + 2*w*h + 2*h*l"

    Parameters
    ----------
    input_data: list
        The list of packages
            20x3x11
             LxWxH

    Returns
    -------
    output_package_wrap: int
    """
    output_package_wrap = 0

    for package in input_data:
        # Split input str into ints
        package_measurements = [int(x) for x in package.split("x")]

        # Perform calculation of formula to get face dimensions
        package_face_lw = package_measurements[0] * package_measurements[1]
        package_face_wh = package_measurements[1] * package_measurements[2]
        package_face_hl = package_measurements[2] * package_measurements[0]

        # Find smallest face
        package_face_smallest = min(package_face_lw, package_face_wh, package_face_hl)

        # Find total total square footage
        # Each face exists twice so *2 required
        package_sum = package_face_lw * 2 + package_face_wh * 2 + package_face_hl * 2

        # Add it to the pile
        output_package_wrap += package_sum + int(package_face_smallest)

    return output_package_wrap


def part_two(input_data: list) -> int:
    """Calculate length of ribbon for all packages

    Parameters
    ----------
    input_data: list
        The list of packages
            20x3x11
             LxWxH

    Returns
    -------
    output_package_ribbon: int
    """
    output_package_ribbon = 0

    for package in input_data:
        # Split input str into ints
        package_measurements = [int(x) for x in package.split("x")]

        # Calculate ribbon length
        # Package volume in cubic feet
        package_volume = package_measurements[0] * package_measurements[1] * package_measurements[2]

        # Strip largest of the sides
        package_measurements.remove(max(package_measurements))

        # Calculate ribbon length for remaining smallest route
        package_circumference = (package_measurements[0] * 2) + (package_measurements[1] * 2)
        output_package_ribbon += package_circumference + package_volume

    return output_package_ribbon


if __name__ == "__main__":
    # Read input from disk cache
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'

    # Parse input into usable format
    with path_inputs.open('r') as f:
        input_data = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Part 01: {part_one(input_data)}')
    print(f'Part 02: {part_two(input_data)}')

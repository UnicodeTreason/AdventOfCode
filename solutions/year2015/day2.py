from pathlib import Path


def calculate(inputData: dict, magic: bool = False) -> int:
    """Calculate square footage of wrapping paper for a package using formula "2*l*w + 2*w*h + 2*h*l"

    Parameters
    ----------
    inputData : dict
        The dict of packages
            20x3x11
             LxWxH
    magic : bool, optional
        A flag used to print the Part 2 output

    Returns
    -------
    int
        magic: False
            The final square footage required for all input packages
        magic: True
            The length of ribbon required for all input packages
    """
    output = 0

    for package in inputData:
        # Split input str into ints
        packageMeasurements = [int(x) for x in package.split("x")]

        # Perform calculation of formula to get face dimensions
        packageFaceLW = packageMeasurements[0] * packageMeasurements[1]
        packageFaceWH = packageMeasurements[1] * packageMeasurements[2]
        packageFaceHL = packageMeasurements[2] * packageMeasurements[0]

        # Find smallest face
        packageFaceSmallest = min(packageFaceLW, packageFaceWH, packageFaceHL)

        # Part 2 Switch
        # Calculate ribbon length
        if magic:
            # Package volume in cubic feet
            packageVolume = packageMeasurements[0] * packageMeasurements[1] * packageMeasurements[2]
            return packageVolume

        # Find total total square footage
        # Each face exists twice so *2 required
        packageSum = packageFaceLW*2 + packageFaceWH*2 + packageFaceHL*2

        # Add it to the pile
        output += packageSum + int(packageFaceSmallest)
    return output


if __name__ == "__main__":
    p = Path(__file__).with_name('day2_input.txt')
    with p.open('r') as f:
        inputData = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(inputData)}')
    print(f'Solution 02: {calculate(inputData,True)}')

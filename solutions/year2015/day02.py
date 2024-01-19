from pathlib import Path


def calculate(inputData: list, magic: bool = False) -> int:
    """Calculate square footage of wrapping paper for a package using formula "2*l*w + 2*w*h + 2*h*l"

    Parameters
    ----------
    inputData : list
        The list of packages
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
    outputPackageWrap = 0
    outputPackageRibbon = 0

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

            # Strip largest of the sides
            packageMeasurements.remove(max(packageMeasurements))

            # Calculate ribbon length for remaining smallest route
            packageCircumference = (packageMeasurements[0] * 2) + (packageMeasurements[1] * 2)
            outputPackageRibbon += packageCircumference + packageVolume

        # Find total total square footage
        # Each face exists twice so *2 required
        packageSum = packageFaceLW * 2 + packageFaceWH * 2 + packageFaceHL * 2

        # Add it to the pile
        outputPackageWrap += packageSum + int(packageFaceSmallest)

    # Part 2 Switch
    # Calculate ribbon length
    if magic:
        return outputPackageRibbon
    else:
        return outputPackageWrap


if __name__ == "__main__":
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'
    with path_inputs.open('r') as f:
        inputData = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(inputData)}')
    print(f'Solution 02: {calculate(inputData,True)}')

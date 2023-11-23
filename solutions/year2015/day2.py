from pathlib import Path


def calculate(inputData, magic=False):
    # Input: lxwxh
    # 2*l*w + 2*w*h + 2*h*l
    # 2*6 + 2*12 + 2*8 = 52
    outputPaper = 0

    for package in inputData:
        # Split input into ints
        packageMeasurements = [int(x) for x in package.split("x")]

        # Math time
        packageLW = 2 * packageMeasurements[0] * packageMeasurements[1]
        packageWH = 2 * packageMeasurements[1] * packageMeasurements[2]
        packageHL = 2 * packageMeasurements[2] * packageMeasurements[0]

        # Bit of logic
        packageSmallestSide = min(packageLW, packageWH, packageHL)
        packageSum = packageLW + packageWH + packageHL

        # Add it to the pile
        outputPaper += packageSum + int((packageSmallestSide / 2))

    return outputPaper


if __name__ == "__main__":
    p = Path(__file__).with_name('day2_input.txt')
    with p.open('r') as f:
        inputData = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(inputData)}')
    print(f'Solution 02: {calculate(inputData,True)}')

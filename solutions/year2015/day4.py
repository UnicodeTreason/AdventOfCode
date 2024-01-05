from pathlib import Path
import hashlib
import re


def calculate(inputData: str, magic: bool = False) -> int:
    """Calculate a mined hash for AdventCoin"

    Parameters
    ----------
    inputData : str
        The str based secret key for mining
            abcdef
    magic : bool, optional
        A flag used to print the Part 2 output

    Returns
    -------
    int
        magic: False
            The lowest number that combines with the secret key to produce output starting with 5 zeroes
        magic: True
            The lowest number that combines with the secret key to produce output starting with 6 zeroes
    """
    outputMineNumber = 0
    hashValid = False

    while not hashValid:
        # Munge secret key and current number together
        hashKey = str(inputData) + str(outputMineNumber)
        hashMD5 = hashlib.md5(hashKey.encode('utf-8')).hexdigest()

        # Part 2 Switch
        if magic:
            regexCount = '0{6}.+'
        else:
            regexCount = '0{5}.+'

        if re.match(regexCount, hashMD5):
            hashValid = True
        else:
            outputMineNumber += 1

    return outputMineNumber


if __name__ == "__main__":
    path_inputs = Path(__file__).parent / 'inputs' / 'day4_input.txt'
    with path_inputs.open('r') as f:
        inputData = f.read()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(inputData)}')
    print(f'Solution 02: {calculate(inputData,True)}')

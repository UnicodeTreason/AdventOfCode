from pathlib import Path
import re


def calculate(inputData: list, magic: bool = False) -> int:
    """Calculate bitwise logic gates and wires

    Parameters
    ----------
    inputData: list
        List of strings containing the following elements:
            wires:
                label: a-z
                signalSource: one (gate/wire/specific value)
                signalDestination: many
            signals: 0-65535
            gates: Raw Signal|AND|OR|NOT|LSHIFT|RSHIFT
    magic: bool, optional
        A flag used to print the Part 2 output

    Returns
    -------
    dict
        magic: False
            The value of each wire
        magic: True
            The TBD
    """

    # NOTES
    # 123 -> x means that the signal 123 is provided to wire x.
    # x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    # p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    # NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

    # ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> i']

    #     # COND01: New signal for wire
    #     search_object = re.search(r'^(?P<signal>\d+)\s-> (?P<wire>\w)$', instruction)
    #     # COND02: AND (Bitwise)
    #     search_object = re.search(r'^(?P<inputx>\w)\s(?P<gate>AND)\s(?P<inputy>\w)\s-> (?P<wire>\w)$', instructio
    #     # COND03: OR (Bitwise)
    #     search_object = re.search(r'^(?P<inputx>\w)\s(?P<gate>OR)\s(?P<inputy>\w)\s-> (?P<wire>\w)$', instruction)
    #     # COND04: NOT (Bitwise)
    #     search_object = re.search(r'^(?P<gate>NOT)\s(?P<inputb>\w)\s-> (?P<wire>\w)$', instruction)
    #     # COND05: LSHIFT (Left-Shift)
    #     search_object = re.search(r'^(?P<inputx>\w)\s(?P<gate>LSHIFT)\s(?P<inputy>\w)\s-> (?P<wire>\w)$', instruction)
    #     # COND05: RSHIFT (Right-Shift)
    #     search_object = re.search(r'^(?P<inputx>\w)\s(?P<gate>RSHIFT)\s(?P<inputy>\w)\s-> (?P<wire>\w)$', instruction)

    # Generate wires data structure
    wires = {}
    wires_solved = {}
    for instruction in inputData:
        print(f'INST: {instruction}')

        # New signal for wire
        search_object = re.search(r'^(?P<signal>\d+)\s-> (?P<wire>\w)$', instruction)
        if search_object:
            wires.update({search_object.group('wire'): int(search_object.group('signal'))})
            wires_solved.update({search_object.group('wire'): int(search_object.group('signal'))})
            continue

        # Wires yet to be calculated
        inputs, outputWire = instruction.split(' -> ')
        wires.update({outputWire: inputs})

    # Calculate wires until complete or heat death of universe.
    #     ForEach wire, are all components solved? If so, solve wire.
    #     Loop until wires_solved = wires length
    while len(wires) != len(wires_solved):
        for wire, value in wires.items():
            # Skip if already solved
            if wire in wires_solved:
                continue

            print(f'Value: {value}')

            # Unpack expression into variables
            # TOOD: Determine less naive way to get inputa
            *inputa, gate, inputb = value.split(' ')

            if len(inputa) > 0:
                inputa = str(inputa[0])
            else:
                inputa = ''

            # Check if required values exist
            if not inputa == '':
                if inputa not in wires_solved:
                    continue

            if not inputb.isnumeric():
                if inputb not in wires_solved:
                    continue

            # Calculate wire
            match gate:
                case 'AND':
                    # 'AND (x & y)'
                    wires_solved.update({wire: int(wires_solved[inputa] & wires_solved[inputb])})
                case 'OR':
                    # 'OR (x | y)'
                    wires_solved.update({wire: int(wires_solved[inputa] | wires_solved[inputb])})
                case 'NOT':
                    # 'NOT (~ y)'
                    # Cant use ~ as integers are not limited to 16 bits in Python
                    wires_solved.update({wire: int((1 << 16) - 1 - wires_solved[inputb])})
                case 'LSHIFT':
                    # 'LSHIFT (x << y)'
                    wires_solved.update({wire: int(wires_solved[inputa] << int(inputb))})
                case 'RSHIFT':
                    # 'RSHIFT (x >> y)'
                    wires_solved.update({wire: int(wires_solved[inputa] >> int(inputb))})
                case _:
                    return 'We shouldnt be here'

    sorteddict = sorted(wires_solved.items())
    return dict(sorteddict)


if __name__ == "__main__":
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'
    with path_inputs.open('r') as f:
        inputData = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(inputData)}')
    print(f'Solution 02: {calculate(inputData,True)}')

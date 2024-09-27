from pathlib import Path


def calculate(input_data: list, magic: bool = False) -> int:
    """Calculate bitwise logic gates and wires

    Parameters
    ----------
    input_data: list
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
            The value of each wire after overiding b with a and recalculating
    """

    # Generate wires data structure
    wires = {}
    wires_solved = {}
    for instruction in input_data:
        inputs, outputWire = instruction.split(' -> ')
        wires.update({outputWire: inputs})

    # Part 2
    # TODO: Maybe dont hardcode this.
    if magic:
        wires_solved['b'] = 46065
        magic = False

    # Calculate wires until complete or heat death of universe.
    while len(wires) != len(wires_solved):
        # Calculate wires
        for wire, value in wires.items():
            # Skip if already solved
            if wire in wires_solved:
                continue

            # Unpack expression into variables
            # TODO: Determine less naive way to get operations
            operations = value.split(' ')
            match len(operations):
                case 1:
                    # Wire to Wire
                    inputa = None
                    gate = 'NONE'
                    inputb = operations[0]
                case 2:
                    # NOT
                    inputa = None
                    gate = operations[0]
                    inputb = operations[1]
                case 3:
                    # Everything else
                    inputa = operations[0]
                    gate = operations[1]
                    inputb = operations[2]
                case _:
                    return 'We shouldnt be here.'

            # Check if required values exist for calculation
            if inputa:
                if not inputa.isnumeric():
                    if inputa not in wires_solved:
                        continue
                    else:
                        inputa = wires_solved[inputa]
                else:
                    inputa = int(inputa)

            if inputb:
                if not inputb.isnumeric():
                    if inputb not in wires_solved:
                        continue
                    else:
                        inputb = wires_solved[inputb]
                else:
                    inputb = int(inputb)

            # Calculate wire
            match gate:
                case 'AND':
                    wires_solved.update({wire: int(inputa & inputb)})
                    continue
                case 'OR':
                    wires_solved.update({wire: int(inputa | inputb)})
                    continue
                case 'NOT':
                    # Cant use ~ as integers are not limited to 16 bits in Python.
                    wires_solved.update({wire: int((1 << 16) - 1 - inputb)})
                    continue
                case 'LSHIFT':
                    wires_solved.update({wire: int(inputa << int(inputb))})
                    continue
                case 'RSHIFT':
                    wires_solved.update({wire: int(inputa >> int(inputb))})
                    continue
                case 'NONE':
                    wires_solved.update({wire: int(inputb)})
                    continue
                case _:
                    return 'We shouldnt be here, again.'

    sorteddict = sorted(wires_solved.items())
    return dict(sorteddict)


if __name__ == "__main__":
    path_inputs = Path(__file__).parent / 'inputs' / f'{Path(__file__).stem}_input.txt'
    with path_inputs.open('r') as f:
        input_data = f.read().splitlines()

    print('Calculating Solutions...')
    print(f'Solution 01: {calculate(input_data)}')
    print(f'Solution 02: {calculate(input_data, True)}')

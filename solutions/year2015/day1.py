def calculate(inputdata):
    # ( means go up a floor
    # ) means go down a floor
    output_floor = 0
    for char in inputdata:
        if char == '(':
            output_floor += 1
        elif char == ')':
            output_floor -= 1
    return output_floor

def compute(target, val, operands):
    if operands == []:
        return target == val
    if val > target:
        return False

    return (
        compute(target, val + operands[0], operands[1:])
        or compute(target, val * operands[0], operands[1:])
        or compute(target, val * pow(10, len(str(operands[0]))) + operands[0], operands[1:])
    )


count = 0
while True:
    try:
        equation = input()
    except EOFError:
        break

    answer, operands = (
        int(equation.split(":")[0]),
        [int(x) for x in equation.split(":")[1].split()],
    )
    if compute(answer, operands[0], operands[1:]):
        count += answer

print(count)

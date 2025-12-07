from operator import add, mul

operands  = []
while True:
    inp = input()
    if inp[0] == '+' or inp[0] == '*':
        operators = inp
        break
    else:
        operands.append(inp)

sum = 0
for i in range(len(operators)):
    if operators[i] == '+':
        currOp = add
        result = 0
    elif operators[i] == '*':
        currOp = mul
        result = 1

    operand = ''.join([x[i] for x in operands]).strip()
    if not operand:
        sum += result
        continue

    result = currOp(result, int(operand))
sum += result

print(sum)


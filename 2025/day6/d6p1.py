from functools import reduce
from operator import add, mul

operands  = []
while True:
    inp = input().split()
    if inp[0] == '+' or inp[0] == '*':
        operators = inp
        break
    else:
        operands.append([int(x) for x in inp])

sum = 0
for i in range(len(operators)):
    if operators[i] == '+':
        sum += reduce(add, [x[i] for x in operands])
    elif operators[i] == '*':
        sum += reduce(mul, [x[i] for x in operands])
print(sum)
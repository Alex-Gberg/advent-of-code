import re

total = 0
enabled = True
while True:
    try:
        memory = input()
    except EOFError:
        break
    for instr in re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)|don\'t\(\)|do\(\)', memory):
        if instr == "do()":
            enabled = True
        elif instr == "don't()":
            enabled = False
        elif enabled:
            operands = [int(y) for y in instr[4:-1].split(',')]
            total += operands[0] * operands[1]
print(total)


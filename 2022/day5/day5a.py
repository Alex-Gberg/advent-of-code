# stacks = [
#   ["Z", "N"],
#   ["M", "C", "D"],
#   ["P"]
# ]

stacks = [
  ["F", "C", "P", "G", "Q", "R"],
  ["W", "T", "C", "P"],
  ["B", "H", "P", "M", "C"],
  ["L", "T", "Q", "S", "M", "P", "R"],
  ["P", "H", "J", "Z", "V", "G", "N"],
  ["D", "P", "J"],
  ["L", "G", "P", "Z", "F", "J", "T", "R"],
  ["N", "L", "H", "C", "F", "P", "T", "J"],
  ["G", "V", "Z", "Q", "H", "T", "C", "W"]
]

inp = input()
while inp != "":
  print(inp)

  try:
    inp = input()
  except:
    break

inp = input()
while True:
  instructions = inp.split()

  for i in range(int(instructions[1])):
    stacks[int(instructions[5])-1].append(stacks[int(instructions[3])-1].pop())

  try:
    inp = input()
  except:
    break

for stack in stacks:
  print(stack[-1], end="")
from dataclasses import dataclass
import math

@dataclass
class Monkey:
  items: list
  operation: str
  test: int
  ifTrue: int
  ifFalse: int
  numInspects: int = 0

def parse():
  monkeys = {}
  inp = input()
  while True:
    inp = inp.split()
    assert inp[0] == "Monkey"
    monkeyN = int(inp[1][:-1])

    items = list(map(int, input()[18:].split(", ")))

    operation = input()[19:]

    inp = input().strip().split()
    test = int(inp[-1])

    inp = input().strip().split()
    ifTrue = int(inp[-1])

    inp = input().strip().split()
    ifFalse = int(inp[-1])

    monkeys[monkeyN] = Monkey(items, operation, test, ifTrue, ifFalse)

    try:
      inp = input()
      assert inp == ""
      inp = input()
    except:
      break
  
  return monkeys


def simulate(monkeys, numRounds, div3):
  lcm = math.lcm(*(map(lambda m : monkeys[m].test, monkeys)))
  for i in range(numRounds):
    for m in range(len(monkeys)):
      currM = monkeys[m]
      currM.items = list(map(eval(f"lambda old : (( {currM.operation} ) {'// 3' if div3 else ''} ) % {lcm}"), currM.items))
      currM.numInspects += len(currM.items)
      for item in currM.items:
        if item % currM.test == 0:
          monkeys[currM.ifTrue].items.append(item)
        else:
          monkeys[currM.ifFalse].items.append(item)
      currM.items.clear()
  
  return monkeys


if __name__ == "__main__":
  monkeys = parse()
  print(monkeys)

  monkeys = simulate(monkeys, 10000, False)
  inspects = list(map(lambda m : monkeys[m].numInspects, monkeys))
  inspects.sort(reverse=True)
  monkeyBusiness = inspects[0] * inspects[1]
  print(f"monkeyBusiness: {monkeyBusiness}")

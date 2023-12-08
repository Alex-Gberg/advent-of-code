from math import lcm

moves = input()

nbrs = dict()
startPos = []

input()
inp = input()
while inp:
    node, nbrList = inp.strip().split('=')
    node = node.strip()
    if node[-1] == "A":
        startPos.append(node)
    nbrList = [x.strip() for x in nbrList.strip(" ()").split(',')]

    nbrs[node] = nbrList

    try:
        inp = input()
    except EOFError:
        break

cycles = []
for pos in startPos:
    currMoveP, steps = 0, 0
    while True:
        pos = nbrs[pos][0 if moves[currMoveP] == "L" else 1]
        steps += 1
        if pos[-1] == "Z":
            cycles.append(steps)
            break
        currMoveP = (currMoveP + 1)%len(moves)
print(lcm(*cycles))
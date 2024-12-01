moves = input()

nbrs = dict()

input()
inp = input()
while inp:
    node, nbrList = inp.strip().split('=')
    node = node.strip()
    nbrList = [x.strip() for x in nbrList.strip(" ()").split(',')]

    nbrs[node] = nbrList

    try:
        inp = input()
    except EOFError:
        break

currPos = "AAA"
currMoveP = 0
steps = 0
while currPos != "ZZZ":
    currPos = nbrs[currPos][0 if moves[currMoveP] == "L" else 1]
    steps += 1
    currMoveP = (currMoveP + 1)%len(moves)
print(steps)

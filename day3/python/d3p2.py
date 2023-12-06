schema = []
while True:
    try:
        schema.append(input().strip())
    except EOFError:
        break

currNum = ''
adjGears = []
gearNbrs = {}
for i, line in enumerate(schema):
    if currNum:
        for gear in adjGears:
            if gear in gearNbrs:
                gearNbrs[gear].append(int(currNum))
            else:
                gearNbrs[gear] = [int(currNum)]
    adjGears = []
    currNum = ''

    for j, pos in enumerate(line):
        if 48 <= ord(pos) <= 57:
            toCheck = []
            if i != 0:
                toCheck.append((i-1,j))
            if i != len(schema)-1:
                toCheck.append((i+1,j))
            if not currNum and j != 0:
                if i != 0:
                    toCheck.append((i-1,j-1))
                toCheck.append((i,j-1))
                if i != len(schema)-1:
                    toCheck.append((i+1,j-1))
            for checkPos in toCheck:
                if schema[checkPos[0]][checkPos[1]] == '*':
                    adjGears.append((checkPos))
                    break
            currNum += pos
        elif currNum:
            if pos == '*':
                adjGears.append((i,j))
            if (schema[i-1][j] == '*' if i != 0 else False):
                adjGears.append((i-1,j))
            if (schema[i+1][j] == '*' if i != len(schema)-1 else False):
                adjGears.append((i+1,j))
            for gear in adjGears:
                if gear in gearNbrs:
                    gearNbrs[gear].append(int(currNum))
                else:
                    gearNbrs[gear] = [int(currNum)]
            adjGears = []
            currNum = ''

total = 0
for gear in gearNbrs:
    nbrs = gearNbrs[gear]
    if len(nbrs) == 2:
        total += nbrs[0] * nbrs[-1]
print(total)


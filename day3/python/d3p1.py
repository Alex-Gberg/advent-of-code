schema = []
while True:
    try:
        schema.append(input().strip())
    except EOFError:
        break

total = 0
currNum = ''
isAdj = False
for i, line in enumerate(schema):
    if currNum and isAdj:
        total += int(currNum)
        isAdj = False
    currNum = ''
    for j, pos in enumerate(line):
        if 48 <= ord(pos) <= 57:
            if not isAdj:
                toCheck = []
                if i != 0:
                    toCheck.append(schema[i-1][j])
                if i != len(schema)-1:
                    toCheck.append(schema[i+1][j])
                if not currNum and j != 0:
                    if i != 0:
                        toCheck.append(schema[i-1][j-1])
                    toCheck.append(schema[i][j-1])
                    if i != len(schema)-1:
                        toCheck.append(schema[i+1][j-1])
                for checkPos in toCheck:
                    if checkPos != '.' and not (48 <= ord(checkPos) <= 57):
                        isAdj = True
                        break
            currNum += pos
        elif currNum:
            if isAdj or pos != '.' or (schema[i-1][j] != '.' if i != 0 else False) or (schema[i+1][j] != '.' if i != len(schema)-1 else False):
                total += int(currNum)
                isAdj = False
            currNum = ''
print(total)


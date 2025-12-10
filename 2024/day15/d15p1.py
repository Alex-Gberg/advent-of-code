map = []
i = 0
while True:
    row = list(input())
    if row == []:
        break
    for j in range(len(row)):
        if row[j] == '@':
            start = (i, j)
    map.append(row)

moves = []
while True:
    try:
        moves.extend(list(input()))
    except EOFError:
        break

pos = [start[0], start[1]]
for m in moves:
    if m == '>':
    elif m == 'v':
    elif m == '<':
    elif m == '^':

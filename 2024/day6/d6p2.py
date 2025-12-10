dirs = ('^', '>', 'V', '<')
map = []
i = 0
while True:
    try:
        row = list(input())
        for j in range(len(row)):
            if row[j] != '.' and row[j] != '#':
                start = [i, j, dirs.index(row[j])]
        map.append(row)
        i += 1
    except EOFError:
        break

count = 0
for x in range(len(map)):
    for y in range(len(map[0])):
        pos = start.copy()

        if map[x][y] != '.':
            continue
    
        map[x][y] = '#'

        visited = set()
        loop = False
        while 0 <= pos[0] < len(map) and 0 <= pos[1] < len(map[0]):
            before = len(visited)
            visited.add((pos[0], pos[1], pos[2]))
            if len(visited) == before:
                loop = True
                break

            if pos[2] == 0:
                if pos[0] == 0:
                    break
                if map[pos[0]-1][pos[1]] == '#':
                    pos[2] = (pos[2] + 1) % len(dirs)
                else:
                    pos[0] -= 1
            elif pos[2] == 1:
                if pos[1] == len(map[0])-1:
                    break
                if map[pos[0]][pos[1]+1] == '#':
                    pos[2] = (pos[2] + 1) % len(dirs)
                else:
                    pos[1] += 1
            elif pos[2] == 2:
                if pos[0] == len(map)-1:
                    break
                if map[pos[0]+1][pos[1]] == '#':
                    pos[2] = (pos[2] + 1) % len(dirs)
                else:
                    pos[0] += 1
            elif pos[2] == 3:
                if pos[1] == 0:
                    break
                if map[pos[0]][pos[1]-1] == '#':
                    pos[2] = (pos[2] + 1) % len(dirs)
                else:
                    pos[1] -= 1
            
        count += 1 if loop else 0
        map[x][y] = '.'

print(count)
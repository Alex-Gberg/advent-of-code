from collections import deque, defaultdict

map = []
while True:
    try:
        map.append(input())
    except EOFError:
        break

total_price = 0
considered = set()
curr_plant = None
plots = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if (i,j) in considered:
            continue
        

        curr_plant = map[i][j]
        curr_region = set()
        curr_region.add((i,j))
        q = deque()
        q.append((i,j))
        sides = defaultdict(list)
        while len(q) > 0:
            curr_node = q.popleft()

            if curr_node[0] > 0 and map[curr_node[0]-1][curr_node[1]] == curr_plant:
                if (curr_node[0]-1, curr_node[1]) not in curr_region:
                    q.append((curr_node[0]-1, curr_node[1]))
                    curr_region.add((curr_node[0]-1, curr_node[1]))
            else:
                sides[0].append((curr_node[0], curr_node[1]))
            if curr_node[1] > 0 and map[curr_node[0]][curr_node[1]-1] == curr_plant:
                if (curr_node[0], curr_node[1]-1) not in curr_region:
                    q.append((curr_node[0], curr_node[1]-1))
                    curr_region.add((curr_node[0], curr_node[1]-1))
            else:
                sides[1].append((curr_node[0], curr_node[1]))
            if curr_node[0] < len(map)-1 and map[curr_node[0]+1][curr_node[1]] == curr_plant:
                if (curr_node[0]+1, curr_node[1]) not in curr_region:
                    q.append((curr_node[0]+1, curr_node[1]))
                    curr_region.add((curr_node[0]+1, curr_node[1]))
            else:
                sides[2].append((curr_node[0], curr_node[1]))
            if curr_node[1] < len(map[0])-1 and map[curr_node[0]][curr_node[1]+1] == curr_plant:
                if (curr_node[0], curr_node[1]+1) not in curr_region:
                    q.append((curr_node[0], curr_node[1]+1))
                    curr_region.add((curr_node[0], curr_node[1]+1))
            else:
                sides[3].append((curr_node[0], curr_node[1]))
        
        total_sides = 0
        for x in range(4):
            curr_sides = 0
            if x%2 == 0:
                sides[x].sort(key=lambda y: y[1])
                sides[x].sort(key=lambda y: y[0])

                curr_axis = sides[x][0][0]
                prev_rank = sides[x][0][1]
                for y in range(1, len(sides[x])):
                    if sides[x][y][0] != curr_axis:
                        curr_sides += 1
                        curr_axis = sides[x][y][0]
                        prev_rank = sides[x][y][1]
                        continue

                    if sides[x][y][1]-1 != prev_rank:
                        curr_sides += 1
                        prev_rank = sides[x][y][1]
                        continue
                    
                    prev_rank = sides[x][y][1]
                curr_sides += 1
            else:
                sides[x].sort(key=lambda y: y[0])
                sides[x].sort(key=lambda y: y[1])

                curr_axis = sides[x][0][1]
                prev_rank = sides[x][0][0]
                for y in range(1, len(sides[x])):
                    if sides[x][y][1] != curr_axis:
                        curr_sides += 1
                        curr_axis = sides[x][y][1]
                        prev_rank = sides[x][y][0]
                        continue

                    if sides[x][y][0]-1 != prev_rank:
                        curr_sides += 1
                        prev_rank = sides[x][y][0]
                        continue

                    prev_rank = sides[x][y][0]
                curr_sides += 1
            total_sides += curr_sides
        
        total_price += total_sides * len(curr_region)
        
        for v in curr_region:
            considered.add(v)

print(total_price)



from collections import deque

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
        perim = 0

        while len(q) > 0:
            curr_node = q.popleft()

            if curr_node[0] > 0 and map[curr_node[0]-1][curr_node[1]] == curr_plant:
                if (curr_node[0]-1, curr_node[1]) not in curr_region:
                    q.append((curr_node[0]-1, curr_node[1]))
                    curr_region.add((curr_node[0]-1, curr_node[1]))
            else:
                perim += 1
            if curr_node[1] > 0 and map[curr_node[0]][curr_node[1]-1] == curr_plant:
                if (curr_node[0], curr_node[1]-1) not in curr_region:
                    q.append((curr_node[0], curr_node[1]-1))
                    curr_region.add((curr_node[0], curr_node[1]-1))
            else:
                perim += 1
            if curr_node[0] < len(map)-1 and map[curr_node[0]+1][curr_node[1]] == curr_plant:
                if (curr_node[0]+1, curr_node[1]) not in curr_region:
                    q.append((curr_node[0]+1, curr_node[1]))
                    curr_region.add((curr_node[0]+1, curr_node[1]))
            else:
                perim += 1
            if curr_node[1] < len(map[0])-1 and map[curr_node[0]][curr_node[1]+1] == curr_plant:
                if (curr_node[0], curr_node[1]+1) not in curr_region:
                    q.append((curr_node[0], curr_node[1]+1))
                    curr_region.add((curr_node[0], curr_node[1]+1))
            else:
                perim += 1
        total_price += perim * len(curr_region)
        
        for v in curr_region:
            considered.add(v)

print(total_price)



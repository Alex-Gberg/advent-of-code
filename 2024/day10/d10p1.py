from collections import deque

map = []
trailheads = []
i = 0
while True:
    try:
        inp = [int(x) if x != '.' else -1 for x in list(input())]
        for j,x in enumerate(inp):
            if x == 0:
                trailheads.append((i,j))

        map.append(inp)
        i += 1
    except:
        break


total_score = 0
for th in trailheads:
    q = deque()
    q.append(th)
    reachable = set()
    while len(q) > 0:
        curr_pos = q.popleft()
        if map[curr_pos[0]][curr_pos[1]] == 9:
            reachable.add(curr_pos)


        if curr_pos[0] > 0 and map[curr_pos[0]][curr_pos[1]] + 1 == map[curr_pos[0]-1][curr_pos[1]]:
                q.append((curr_pos[0]-1, curr_pos[1]))
        if curr_pos[1] > 0 and map[curr_pos[0]][curr_pos[1]] + 1 == map[curr_pos[0]][curr_pos[1]-1]:
                q.append((curr_pos[0], curr_pos[1]-1))
        if curr_pos[0] < len(map)-1 and map[curr_pos[0]][curr_pos[1]] + 1 == map[curr_pos[0]+1][curr_pos[1]]:
                q.append((curr_pos[0]+1, curr_pos[1]))
        if curr_pos[1] < len(map[0])-1 and map[curr_pos[0]][curr_pos[1]] + 1 == map[curr_pos[0]][curr_pos[1]+1]:
                q.append((curr_pos[0], curr_pos[1]+1))
    total_score += len(reachable)


print(total_score)
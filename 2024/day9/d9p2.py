from collections import defaultdict

map = input()

blocks = [[x//2 if x%2==0 else -1, int(map[x])] for x in range(len(map))]

i = len(blocks)-1
handled = set()
while i > 0:
    if blocks[i][0] == -1 or blocks[i][0] in handled:
        i -= 1
        continue

    moved = False
    for j in range(i):
        if blocks[j][0] == -1 and blocks[j][1] >= blocks[i][1]:
            curr_idx = blocks[i][0]
            handled.add(curr_idx)
            blocks[j][1] -= blocks[i][1]
            blocks[i][0] = -1
            blocks.insert(j, [curr_idx, blocks[i][1]])
            moved = True
            break
    if not moved:
        i -= 1

checksum = 0
i = 0
for b in blocks:
    if b[0] == -1:
        i += b[1]
        continue
    for x in range(b[1]):
        checksum += b[0] * i
        i += 1


print(checksum)

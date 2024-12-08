from collections import defaultdict

width, height = 0, 0
antennas = defaultdict(list)
while True:
    try:
        row = input()
        for x in range(len(row)):
            if row[x] != '.' and row[x] != '#':
                antennas[row[x]].append((height,x))
        width = len(row)
        height += 1
    except EOFError:
        break

anodes = set()
for freq in antennas:
    for i in range(len(antennas[freq])-1):
        for j in range(i+1, len(antennas[freq])):
            dx, dy = antennas[freq][i][0] - antennas[freq][j][0], antennas[freq][i][1] - antennas[freq][j][1]
            mul = 0
            while 0 <= antennas[freq][i][0] + (dx*mul) < height and 0 <= antennas[freq][i][1] + (dy*mul) < width:
                anodes.add((antennas[freq][i][0] + (dx*mul), antennas[freq][i][1] + (dy*mul)))
                mul += 1
            mul = 0
            while 0 <= antennas[freq][j][0] - (dx*mul) < height and 0 <= antennas[freq][j][1] - (dy*mul) < width:
                anodes.add((antennas[freq][j][0] - (dx*mul), antennas[freq][j][1] - (dy*mul)))
                mul += 1

print(len(anodes))



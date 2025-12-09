from functools import reduce

def printGrid(grid):
  print("==== Grid ====")
  for g in grid:
    for p in g:
      print(p, end="")
    print()

# parse lines and find ranges
lines = []
xMin, yMin = 10000, 10000
xMax, yMax = -1, -1
while True:
  try:
    inp = input()
  except:
    break

  line = list(map(lambda x : list(map(int, x.split(","))), inp.split(" -> ")))
  lines.append(line)

  for l in line:
    if l[0] < xMin:
      xMin = l[0]
    if l[0] > xMax:
      xMax = l[0]
    if l[1] < yMin:
      yMin = l[1]
    if l[1] > yMax:
      yMax = l[1]
print(f"x: [{xMin}, {xMax}]\ny: [{yMin}, {yMax}]")

# make an empty grid of required size
grid = [["." for x in range((xMax-xMin)+1)] for y in range(yMax+1)]

# find sand entry
sandEntry = [500-xMin, 0]
grid[sandEntry[1]][sandEntry[0]] = "V"
print(f"sand entry: {sandEntry}")

# prepare grid
for line in lines:
  for i in range(len(line)):
    # normalize values
    line[i][0] -= xMin

    # populate grid
    if i > 0:
      if line[i][0] == line[i-1][0]:
        lBound, uBound = (line[i-1][1], line[i][1]+1) if line[i-1][1] < line[i][1] else (line[i][1], line[i-1][1]+1)
        for j in range(lBound, uBound):
          grid[j][line[i][0]] = "#"
      else:
        lBound, uBound = (line[i-1][0], line[i][0]+1) if line[i-1][0] < line[i][0] else (line[i][0], line[i-1][0]+1)
        grid[line[i][1]][lBound:uBound] = ["#"] * (abs(line[i-1][0]-line[i][0])+1)
printGrid(grid)

# part 1: simulate sand
# TODO: implement a stack of positions, push when reaching a new pos, pop when the sand has settled
sCount = 0
pos = list(sandEntry)
lPos = list(pos)
while True:
  if pos[1] + 1 >= len(grid) or pos[0] < 0 or pos[0] >= len(grid[0]):
    break
  if grid[pos[1]+1][pos[0]] == ".":
    lPos[0], lPos[1] = pos[0], pos[1]
    pos[1] += 1
  elif grid[pos[1]+1][pos[0]-1] == ".":
    lPos[0], lPos[1] = pos[0], pos[1]
    pos[1] += 1
    pos[0] -= 1
  elif grid[pos[1]+1][pos[0]+1] == ".":
    lPos[0], lPos[1] = pos[0], pos[1]
    pos[1] += 1
    pos[0] += 1
  else:
    grid[pos[1]][pos[0]] = "o"
    sCount += 1
    if lPos[0] != -1:
      pos[0], pos[1] = lPos[0], lPos[1]
      lPos = [-1,-1]
    else:
      pos = list(sandEntry)
printGrid(grid)
print(f"sand count: {sCount}")

# part 2: count sand in full pyramid
# formula: numSand = fullPyramid - rocks - gaps (upside down pyramids)
height = len(grid)+1
base = (height*2)-1
fullPyramid = reduce(lambda a, x: a+x, range(1, base+1, 2))

grid.append(["."] * len(grid[0]))
numRocks = 0
numGaps = 0
for i in range(1, len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == "#":
      numRocks += 1
    elif 0 < j < len(grid[0])-1 and grid[i][j] == "." and (grid[i-1][j-1] == "#" or grid[i-1][j-1] == "x") and (grid[i-1][j] == "#" or grid[i-1][j] == "x") and (grid[i-1][j+1] == "#" or grid[i-1][j+1] == "x"):
      grid[i][j] = "x"
      numGaps += 1
printGrid(grid)
print(f"sand count: {fullPyramid-numRocks-numGaps}")

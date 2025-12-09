from collections import deque

grid = []
while True:
  try:
    grid.append(input())
  except:
    break

dirs = {
  "up": [-1,0],
  "right": [0,1],
  "down": [1,0],
  "left": [0,-1]
}

startingPoints = []
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == "S":
      start = [i,j]
      startingPoints.append([i,j])
      grid[i] = grid[i].replace("S", "a")
    elif grid[i][j] == "E":
      end = [i,j]
      grid[i] = grid[i].replace("E", "z")
    elif grid[i][j] == "a":
      startingPoints.append([i,j])
print(f"start: {start}, end: {end}")

neighbors = {}
for i in range(len(grid)):
  for j in range(len(grid[0])):
    currNbs = []
    currVal = ord(grid[i][j])
    for d in dirs:
      nbI, nbJ = i+dirs[d][0], j+dirs[d][1]
      if 0 <= nbI < len(grid) and 0 <= nbJ < len(grid[0]):
        nbVal = ord(grid[nbI][nbJ])
        if nbVal <= currVal+1:
          currNbs.append([nbI,nbJ])
    neighbors[str([i,j])] = currNbs

def bfs(neighbors, start, end):
  q = deque()
  visited = set()
  distances = {x: float('inf') for x in neighbors}

  distances[str(start)] = 0
  visited.add(str(start))
  q.append(start)

  while q:
    currNode = q.popleft()
    for n in neighbors[str(currNode)]:
      if str(n) not in visited:
        visited.add(str(n))
        distances[str(n)] = distances[str(currNode)] + 1
        q.append(n)

        if n == end:
          return distances[str(end)]
  return distances[str(end)]


print("Shortest distance from \"S\" to \"E\":", bfs(neighbors, start, end))

bestHike = float('inf')
for i, s in enumerate(startingPoints):
  print('Calculating best hike (%d/%d)\r' %(i+1, len(startingPoints)), end="")
  hike = bfs(neighbors, s, end)
  if hike < bestHike:
    bestHike = hike
print("Shortest distance from any \"a\" to \"E\":", bestHike)

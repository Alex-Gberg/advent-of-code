def manDist(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

# y = 10
y = 2000000

sensors = []
beacons = []

minX, maxX = float('inf'), -float('inf')
while True:
  try:
    inp = input().split()
  except:
    break

  sens = [int(inp[2][2:-1]), int(inp[3][2:-1])]
  beac = [int(inp[-2][2:-1]), int(inp[-1][2:])]
  manhattanDist = manDist(sens, beac)

  if sens[0]-manhattanDist < minX:
    minX = sens[0] - manhattanDist
  if sens[0]+manhattanDist > maxX:
    maxX = sens[0] + manhattanDist

  sensors.append((sens, manhattanDist))
  beacons.append(beac)

# part 1
count = 0
for x in range(int(minX), int(maxX+1)):
  if [x, y] in beacons:
    continue
  for s in sensors:
    if manDist([x, y], s[0]) <= s[1]:
      count += 1
      break
print(f"# non-beacons at y={y}: {count}")

# part 2
# searchRange = [0,20]
searchRange = [0, 4000000]
print(f"search range: {searchRange}")
for x in range(searchRange[0], searchRange[1]+1):
  for y in range(searchRange[0], searchRange[1]+1):
    print(('[%d,%d]\r' %(x, y)), end="")
    candidate = True
    for i, s in enumerate(sensors):
      if manDist([x, y], s[0]) <= s[1]:
        candidate = False
        break
    if candidate:
      print(f"tuning frequency: {(x*4000000)+y}")
      exit()
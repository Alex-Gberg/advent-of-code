import math

numKnots = 10

knotPos = [[0,0] for _ in range(numKnots)]

tailVisited = {str([0,0]): 1}
numVisited = 1

dirMap = {
  "R": [1,0],
  "RU": [1,1],
  "RD": [1,-1],
  "L": [-1,0],
  "LU": [-1,1],
  "LD": [-1,-1],
  "U": [0,1],
  "D": [0,-1],
}

def pointDist(x, y):
  return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

while True:
  try:
    inp = input()
  except:
    break

  dir, dist = inp.split()

  for i in range(int(dist)):
    knotPos[0] = [x+y for x, y in zip(knotPos[0], dirMap[dir])]
    for j in range(1, numKnots):
      if pointDist(knotPos[j-1], knotPos[j]) >= 2:
        bestPos = knotPos[j]
        bestDist = 2
        for k in dirMap:
          tempPos = [x+y for x, y in zip(knotPos[j], dirMap[k])]
          tempDist = pointDist(knotPos[j-1], tempPos)
          if tempDist < bestDist:
            bestPos = tempPos
            bestDist = tempDist
        knotPos[j] = bestPos

    if str(knotPos[-1]) not in tailVisited:
      tailVisited[str(knotPos[-1])] = 1
      numVisited += 1

print(numVisited)
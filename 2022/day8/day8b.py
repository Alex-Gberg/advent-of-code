def getGrid():
  grid = []

  while True:
    try:
      inp = input()
      grid.append(inp)
    except:
      break

  return grid

def findBestScore(grid):
  bestScore = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):

      rScore = 0
      for r in range(j+1,len(grid)):
        rScore += 1
        if int(grid[i][r]) >= int(grid[i][j]):
          break

      dScore = 0
      for d in range(i+1,len(grid[0])):
        dScore += 1
        if int(grid[d][j]) >= int(grid[i][j]):
          break

      lScore = 0
      for l in range(j-1, -1, -1):
        lScore += 1
        if int(grid[i][l]) >= int(grid[i][j]):
          break

      uScore = 0
      for u in range(i-1, -1, -1):
        uScore += 1
        if int(grid[u][j]) >= int(grid[i][j]):
          break
      
      currScore = rScore * dScore * lScore * uScore
      if currScore > bestScore:
        bestScore = currScore

  return bestScore

if __name__ == "__main__":
  grid = getGrid()
  score = findBestScore(grid)
  print(score)

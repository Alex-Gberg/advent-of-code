# top-down DP
# pre compute tallest tree in a certain direction from a certain point
# += if there is a direction with a max tree height less than current pos


def getGrid():
  grid = []

  while True:
    try:
      inp = input()
      grid.append(inp)
    except:
      break

  return grid

dirMap = {
  "top": 0,
  "bottom": 1,
  "left": 2,
  "right": 3
}

def makeDP(grid):
  dp = [[[-1,-1,-1,-1] for pos in row] for row in grid]
  
  # from the left and top
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if i == 0:
        dp[i][j][dirMap["top"]] = -1
      else:
        dp[i][j][dirMap["top"]] = max(dp[i-1][j][dirMap["top"]], int(grid[i-1][j]))
      if j == 0:
        dp[i][j][dirMap["left"]] = -1
      else:
        dp[i][j][dirMap["left"]] = max(dp[i][j-1][dirMap["left"]], int(grid[i][j-1]))

  # from the right and bottom
  for i in range(len(grid)-1, -1, -1):
    for j in range(len(grid[0])-1, -1, -1):
      if i == len(grid)-1:
        dp[i][j][dirMap["bottom"]] = -1
      else:
        dp[i][j][dirMap["bottom"]] = max(dp[i+1][j][dirMap["bottom"]], int(grid[i+1][j]))
      if j == len(grid[0])-1:
        dp[i][j][dirMap["right"]] = -1
      else:
        dp[i][j][dirMap["right"]] = max(dp[i][j+1][dirMap["right"]], int(grid[i][j+1]))
  
  return dp

def countVisible(grid, dp):
  count = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if int(grid[i][j]) > min(dp[i][j][dirMap["left"]], dp[i][j][dirMap["top"]], dp[i][j][dirMap["right"]], dp[i][j][dirMap["bottom"]]):
        count += 1

  return count

if __name__ == "__main__":
  grid = getGrid()
  dp = makeDP(grid)
  numVisible = countVisible(grid, dp)
  print(f"numVisible={numVisible}")
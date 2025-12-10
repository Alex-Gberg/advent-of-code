equiv = {
  "A": "X",
  "B": "Y",
  "C": "Z"
}

beats = {
  "X": "C",
  "Y": "A",
  "Z": "B"
}

shapePoints = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

gamePoints = {
  "lose": 0,
  "draw": 3,
  "win": 6
}

inp = input()
score = 0
while True:
  theirs, mine = inp.split()
  score += shapePoints[mine]
  score += gamePoints["win"] if beats[mine] == theirs else gamePoints["draw"] if equiv[theirs] == mine else gamePoints["lose"]
  
  try:
    inp = input()
  except:
    break

print(score)
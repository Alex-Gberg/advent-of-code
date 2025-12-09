outcome = {
  "X": "lose",
  "Y": "draw",
  "Z": "win"
}

shapePoints = {
    "A": 1,
    "B": 2,
    "C": 3
}

gamePoints = {
    "lose": 0,
    "draw": 3,
    "win": 6
}

beats = {
  "A": "B",
  "B": "C",
  "C": "A"
}

loses = {
  "A": "C",
  "B": "A",
  "C": "B"
}

inp = input()
score = 0
while True:
  theirs, reqOut = inp.split()
  score += gamePoints[outcome[reqOut]]
  if reqOut == "Z":
    score += shapePoints[beats[theirs]]
  elif reqOut == "Y":
    score += shapePoints[theirs]
  elif reqOut == "X":
    score += shapePoints[loses[theirs]]


  try:
    inp = input()
  except:
    break

print(score)

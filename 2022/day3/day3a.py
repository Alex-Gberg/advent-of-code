inp = input()
priScore = 0
while True:
  l = len(inp)
  hash = {}
  for i in range(l//2):
    if inp[i] in hash:
      hash[inp[i]] += 1
    else:
      hash[inp[i]] = 1
  for i in range(l//2, l):
    if inp[i] in hash:
      if ord(inp[i]) < 91:
        priScore += ord(inp[i]) - 38
      else:
        priScore += ord(inp[i]) - 96
      break

  try:
    inp = input()
  except:
    break
print(priScore)
inp = input()

for i, a in enumerate(inp):
  freq = {}
  for j in range(4):
    if inp[i+j] in freq:
      break
    else:
      freq[inp[i+j]] = 1
  if len(freq) == 4:
    print(i+4)
    break
  
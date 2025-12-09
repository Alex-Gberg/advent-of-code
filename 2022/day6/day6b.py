inp = input()

for i, a in enumerate(inp):
  freq = {}
  for j in range(14):
    # print(f"i:{i}; j:{j}")
    # print(inp[i+j])
    if inp[i+j] in freq:
      break
    else:
      freq[inp[i+j]] = 1
  if len(freq) == 14:
    print(i+14)
    break

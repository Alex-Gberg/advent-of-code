inp = input()
score = 0
while True:
  elves = [inp, input(), input()]
  frequencies = {}
  for elf in elves:
    individualFrequencies = {}
    for i in elf:
      if i in individualFrequencies:
        continue
      else:
        individualFrequencies[i] = 1
        if i in frequencies:
          frequencies[i] += 1
          if frequencies[i] == 3:
            if ord(i) < 91:
              score += ord(i) - 38
            else:
              score += ord(i) - 96
            break
        else:
          frequencies[i] = 1
  try:
    inp = input()
  except:
    break
print(score)

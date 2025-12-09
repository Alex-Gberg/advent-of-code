count = 0
inp = input()
while True:
  elf1, elf2 = inp.split(",")
  elf1 = list(map(int, elf1.split("-")))
  elf2 = list(map(int, elf2.split("-")))
  
  if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
    count += 1
  elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
    count += 1

  try:
    inp = input()
  except:
    break
print(count)

cycles = [20,60,100,140,180,220]
cPointer = 0

x = 1
op = None

strengths = 0
cycle = 1
while True:
  if cPointer != len(cycles) and cycle == cycles[cPointer]:
    strengths += cycle * x
    cPointer += 1

  pos = (cycle-1) % 40
  chr = "_"
  if x-1 <= pos <= x+1:
    chr = "0"
  print(chr, end="\n" if cycle%40 == 0 else "")

  if not op:
    try:
      inp = input()
    except:
      break
  
    inp = inp.split()
    if inp[0] != "noop":
      op = int(inp[1])
  else:
    x += op
    op = None
  
  cycle += 1

print(f"signal strengths: {strengths}")
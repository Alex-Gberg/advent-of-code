from itertools import zip_longest

def parse(inp):
  arrayStack = []
  numb = ""
  for i, c in enumerate(inp):
    if c == "[":
      newList = []
      if arrayStack:
        arrayStack[-1].append(newList)
      arrayStack.append(newList)
    elif c == "]":
      if numb:
        arrayStack[-1].append(int(numb))
        numb = ""
      if i == len(inp)-1:
        return arrayStack.pop()
      arrayStack.pop()
    elif c == ",":
      if numb:
        arrayStack[-1].append(int(numb))
        numb = ""
    else:
      numb += c

def compare(left, right):
  for i, j in zip_longest(left, right):
    if i == None:
      return True
    elif j == None:
      return False
    if type(i) == type(j):
      if type(i) == int:
        if i < j:
          return True
        elif i > j:
          return False
        else:
          continue
      elif type(i) == list:
        res = compare(i, j)
        if res != None:
          return res
    else:
      if type(i) == int:
        res = compare([i], j)
        if res != None:
          return res
      else:
        res = compare(i, [j])
        if res != None:
          return res
  return None

def bubbleSort(list):
  for i in range(len(packets)-1, -1, -1):
    for j in range(i):
      if not compare(packets[j], packets[j+1]):
        packets[j], packets[j+1] = packets[j+1], packets[j]

def mergeSort(list, comp):
  if len(list) <= 1:
    return list
  else:
    return merge(mergeSort(list[:len(list)//2], comp), mergeSort(list[len(list)//2:], comp), comp)

def merge(l1, l2, comp):
  l1Pointer = 0
  l2Pointer = 0

  mergedL = []

  while l1Pointer != len(l1) or l2Pointer != len(l2):
    if l1Pointer == len(l1):
      mergedL.extend(l2[l2Pointer:])
      l2Pointer = len(l2)
    elif l2Pointer == len(l2):
      mergedL.extend(l1[l1Pointer:])
      l1Pointer = len(l1)
    elif comp(l1[l1Pointer], l2[l2Pointer]):
      mergedL.append(l1[l1Pointer])
      l1Pointer += 1
    else:
      mergedL.append(l2[l2Pointer])
      l2Pointer += 1

  return mergedL



if __name__ == "__main__":
  packet1 = input()
  packet2 = input()
  i = 1
  count = 0
  packets = []
  while True:
    packet1 = parse(packet1)
    packet2 = parse(packet2)

    packets.append(packet1)
    packets.append(packet2)

    if compare(packet1, packet2):
      count += i

    try:
      input()
      packet1 = input()
      packet2 = input()
      i += 1
    except:
      break
  print(f"sum of indices: {count}")

  packets.extend([[[2]], [[6]]])
  # bubbleSort(packets)
  packets = mergeSort(packets, compare)
  i1 = packets.index([[2]])
  i2 = packets.index([[6]])
  print(f"decoder key: {(i1+1) * (i2+1)}")

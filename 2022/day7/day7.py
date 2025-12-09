def makeDirStructure():
  inp = input()
  files = {"/":{}}
  pathStack = []
  currDir = files
  while True:
    inp = inp.split()
    if inp[0] == "$":
      if inp[1] == "cd":
        if inp[2] == "..":
          pathStack.pop()
        else:
          pathStack.append(inp[2])
      elif inp[1] == "ls":
        currDir = files
        for p in pathStack:
          currDir = currDir[p]
    else:
      if inp[0] == "dir":
        currDir[inp[1]] = {}
      else:
        currDir[inp[1]] = int(inp[0])  # type: ignore

    try:
      inp = input()
    except:
      break
  return files

def countSizes(files, sum):
  size = 0
  for el in files:
    if isinstance(files[el], int):
      size += files[el]
    else:
      subSize, sum = countSizes(files[el], sum)
      size += subSize

  if size <= 100000:
    sum += size
  return size, sum

def findDirToDelete(files, requiredSpace, currBest):
  size = 0
  for el in files:
    if isinstance(files[el], int):
      size += files[el]
    else:
      subSize, _, currBest = findDirToDelete(files[el], requiredSpace, currBest)
      size += subSize
  
  if currBest > size >= requiredSpace:
    currBest = size
  return size, requiredSpace, currBest

if __name__ == "__main__":
  files = makeDirStructure()
  totalSize, sum = countSizes(files["/"], 0)
  print(f"total size: {totalSize}\nsum of dirs under 100,000: {sum}")
  sizeOfDeletion = findDirToDelete(files, 30000000-(70000000-totalSize), 70000001)
  print(f"size of dir to delete: {sizeOfDeletion[2]}")

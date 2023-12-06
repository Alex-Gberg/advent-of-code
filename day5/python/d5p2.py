seedInfo = [int(x) for x in input().strip().split(':')[1].strip().split()]
seedRanges = [(seedInfo[i], seedInfo[i]+seedInfo[i+1]-1) for i in range(0, len(seedInfo),2)]
seedRanges.sort(key=lambda x: x[0])
input()

maps = []
while True:
    try:
        input()
    except EOFError:
        break

    map = []
    inp = input()
    while inp:
        destStart, sourceStart, rLength = [int(x) for x in inp.strip().split()]
        map.append((sourceStart, sourceStart+rLength-1, destStart-sourceStart))

        try:
            inp = input()
        except EOFError:
            break
    map.sort(key=lambda x: x[0])
    maps.append(map)

locations = []
mapPointer = 0
for r in seedRanges:
    rL = r[0]
    rR = r[1]
    newRanges = []
    for i in range(mapPointer,):
        if rR < maps[i][0]:
            newRanges.append((rL, rR))
            mapPointer = i
            break
        if rL > maps[i][1]:
            continue
        if maps[i][0] <= rL and rR <= maps[i][1]:
            newRanges.append((rL+maps[i][2], rR+maps[i][2]))
            mapPointer = i
            break
        if rL <= maps[i][1]:
            





        mapPointer = i

print(min(locations))

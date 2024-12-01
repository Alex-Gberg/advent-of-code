seedInfo = [int(x) for x in input().strip().split(':')[1].strip().split()]
seedRanges = [(seedInfo[i], seedInfo[i]+seedInfo[i+1]-1) for i in range(0, len(seedInfo), 2)]
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


ranges = seedRanges
for stage in maps:
    newRanges = []
    mapPointer = 0
    for r in ranges:
        rL = r[0]
        rR = r[1]
        for i in range(mapPointer, len(stage)):
            if rL > rR:
                break
            if rR < stage[i][0]:
                newRanges.append((rL, rR))
                mapPointer = i
                break
            if rL > stage[i][1]:
                if i == len(stage)-1:
                    newRanges.append((rL, rR))
                    mapPointer = i
                    break
                continue
            if rL < stage[i][0]:
                newRanges.append((rL, stage[i][0]-1))
                if rR <= stage[i][1]:
                    newRanges.append((stage[i][0]+stage[i][2], rR+stage[i][2]))
                    mapPointer = i
                    break
                else:
                    newRanges.append((stage[i][0]+stage[i][2], stage[i][1]+stage[i][2]))
                    rL = stage[i][1]+1
                    continue
            if rL >= stage[i][0]:
                if rR <= stage[i][1]:
                    newRanges.append((rL+stage[i][2], rR+stage[i][2]))
                    mapPointer = i
                    break
                else:
                    newRanges.append((rL+stage[i][2], stage[i][1]+stage[i][2]))
                    rL = stage[i][1]+1
                    continue
    newRanges.sort(key=lambda x: x[0])
    ranges = newRanges
print(ranges[0][0])

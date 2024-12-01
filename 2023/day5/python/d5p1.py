seeds = [int(x) for x in input().strip().split(':')[1].strip().split()]
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
for seed in seeds:
    val = seed
    for map in maps:
        offset = None
        l = 0
        r = len(map)-1
        while not r<l:
            m = l+(r-l)//2
            guess = map[m]
            if guess[0] <= val <= guess[1]:
                offset = guess[2]
                break
            elif guess[0] < val:
                l = m+1
            elif guess[0] > val:
                r = m-1
        val = val+offset if offset else val

    locations.append(val)
print(min(locations))

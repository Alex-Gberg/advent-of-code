numSafe = 0
while True:
    try:
        levels = [int(x) for x in input().split()]
    except EOFError:
        break

    increasing = True if levels[0] < levels[1] else False
    safe = True
    for i in range(1,len(levels)):
        if (increasing and not (3 >= levels[i] - levels[i-1] >= 1)) or (not increasing and not (3 >= levels[i-1] - levels[i] >= 1)):
                safe = False
                break
    numSafe += 1 if safe else 0

print(numSafe)









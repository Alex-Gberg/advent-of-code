ranges = []
while True:
    inp = input()
    if inp == '':
        break

    currRange = [int(x) for x in inp.split('-')]
    toRemove = []
    for r in ranges:
        if not (r[1] < currRange[0] or currRange[1] < r[0]):
            currRange = [min(r[0], currRange[0]), max(r[1], currRange[1])]
            toRemove.append(r)
    for r in toRemove:
        ranges.remove(r)
    ranges.append(currRange)

count = 0
for r in ranges:
    count += r[1] - r[0] + 1
print(count)

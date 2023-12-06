sum = 0

inp = input()
while inp:
    minimums = {'red': 0, 'green': 0, 'blue': 0}
    for round in inp.strip().split(':')[1].split(';'):
        for color in round.split(','):
            colorCount = color.strip().split()
            if int(colorCount[0]) > minimums[colorCount[1]]:
                minimums[colorCount[1]] = int(colorCount[0])

    power = 1
    for m in minimums.values():
        power *= m
    sum += power

    try:
        inp = input()
    except:
        break
print(sum)
colorMap = {'red': 12, 'green': 13, 'blue': 14}

sum = 0

inp = input()
while inp:
    game = inp.strip().split(':')
    id = int(game[0].split()[1])
    roundFailed = False
    for round in game[1].split(';'):
        for color in round.split(','):
            colorCount = color.strip().split()
            if int(colorCount[0]) > colorMap[colorCount[1]]:
                roundFailed = True
                break
        if roundFailed:
            break
    if not roundFailed:
        sum += id

    try:
        inp = input()
    except:
        break
print(sum)
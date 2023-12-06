inp = input()

cards = {}
while inp:
    matches = 0
    inp = inp.strip().split(':') 
    gameNo = int(inp[0].split()[1])
    if gameNo in cards:
        cards[gameNo] += 1
    else:
        cards[gameNo] = 1

    mult = cards[gameNo]

    game = inp[1].strip().split('|')
    s = {x for x in game[0].strip().split()}
    for x in game[1].strip().split():
        if x in s:
            matches += 1

    for x in range(gameNo+1, gameNo+matches+1):
        if x in cards:
            cards[x] += 1*mult
        else:
            cards[x] = 1*mult

    try:
        inp = input()
    except:
        break

print(sum(cards.values()))
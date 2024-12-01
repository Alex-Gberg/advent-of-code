from functools import cmp_to_key

hands = []

inp = input()
while inp:
    inp = inp.strip().split()
    hands.append((inp[0], int(inp[1])))

    try:
        inp = input()
    except EOFError:
        break

def getHandType(hand):
    dic = dict()
    for card in hand:
        if card in dic:
            dic[card] += 1
        else:
            dic[card] = 1
    
    if len(dic) == 1:
        return 7
    elif len(dic) == 2:
        if 4 in dic.values():
            return 6
        else:
            return 5
    elif len(dic) == 3:
        if 3 in dic.values():
            return 4
        else:
            return 3
    elif len(dic) == 4:
        return 2
    else:
        return 1

cardStrength = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

def compareHands(hand1, hand2):
    hand1, hand2 = hand1[0], hand2[0]
    handDif = getHandType(hand1) - getHandType(hand2)
    if handDif > 0:
        return 1
    elif handDif < 0:
        return -1
    else:
        for c1, c2 in zip(hand1, hand2):
            if c1 == c2:
                continue
            c1, c2 = [int(x) if x.isnumeric() else cardStrength[x] for x in [c1,c2]]
            if c1 > c2:
                return 1
            else:
                return -1
        return 0

hands.sort(key=cmp_to_key(compareHands))
print(sum([hand[1]*(rank+1) for rank, hand in enumerate(hands)]))
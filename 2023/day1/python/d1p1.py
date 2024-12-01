inp = input()
total = 0
while inp:
    term = 0
    for x, inpt in enumerate([inp, inp[::-1]]):
        for a in inpt:
            if 48 <= ord(a) <= 57:
                term += int(a) * (10 if x == 0 else 1)
                break
    total += term
    try:
        inp = input()
    except:
        break
print(total)
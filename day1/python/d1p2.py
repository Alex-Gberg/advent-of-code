digitMap = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

inp = input()
total = 0
while inp:
    term = 0
    for x, inpt in enumerate([inp, inp[::-1]]):
        for i, a in enumerate(inpt):
            if i > 1:
                for j in range(i-1):
                    s = inpt[j:i+1] if x == 0 else inpt[j:i+1][::-1]
                    if s in digitMap:
                        term += digitMap[s] * (10 if x == 0 else 1)
                        break
            if str(term)[x] != "0":
                break
            if 48 <= ord(a) <= 57:
                term += int(a) * (10 if x == 0 else 1)
                break
    total += term
    try:
        inp = input()
    except:
        break
print(total)
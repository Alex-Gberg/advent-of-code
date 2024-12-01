inp = input()

total = 0
while inp:
    score = 0
    inp = inp.strip().split(':')[1].strip().split('|')
    s = {x for x in inp[0].strip().split()}
    for x in inp[1].strip().split():
        if x in s:
            if score == 0:
                score = 1
            else:
                score *= 2
    total += score

    try:
        inp = input()
    except:
        break
print(total)
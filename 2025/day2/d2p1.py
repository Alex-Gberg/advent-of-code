count = 0
ranges = [[int(y) for y in x.split('-')] for x in input().split(',')]
for r in ranges:
    if len(str(r[0])) == len(str(r[1])) and len(str(r[0])) % 2 == 1:
        continue
    for i in range(r[0], r[1]+1):
        istr = str(i)
        if len(istr) % 2 == 1:
            continue
        if istr[:len(istr)//2] == istr[len(istr)//2:]:
            count += i
print(count)
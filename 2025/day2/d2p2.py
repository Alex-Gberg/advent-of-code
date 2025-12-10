count = 0
ranges = [[int(y) for y in x.split('-')] for x in input().split(',')]
for r in ranges:
    for i in range(r[0], r[1]+1):
        invalid = False
        istr = str(i)
        lenistr = len(str(i))
        for j in range(1, (lenistr//2)+1):
            if lenistr % j == 0:
                isSeq = True
                seq = istr[:j]
                for c in range(j,len(istr)-j+1, j):
                    if istr[c:c+j] != seq:
                        isSeq = False
                        break
                if isSeq:
                    invalid = True
                    break
        if invalid:
            count += i
print(count)
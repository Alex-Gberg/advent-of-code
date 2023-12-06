time = int(''.join(input().strip().split(":")[1].strip().split()))
distance = int(''.join(input().strip().split(":")[1].strip().split()))

l1 = 1
r1 = time
while l1<=r1:
    guess = l1+(r1-l1)//2
    if (time-guess)*guess > distance:
        r1 = guess-1
        continue
    if (time-guess)*guess <= distance:
        l1 = guess+1

l2 = 1
r2 = time
while l2<=r2:
    guess = l2+(r2-l2)//2
    if (time-guess)*guess > distance:
        l2 = guess+1
        continue
    if (time-guess)*guess <= distance:
        r2 = guess-1

print(r2-r1)
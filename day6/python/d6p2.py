time = int(''.join(input().strip().split(":")[1].strip().split()))
distance = int(''.join(input().strip().split(":")[1].strip().split()))

waysToWin = 0
for i in range(1,time+1):
    if (time-i)*i > distance:
        waysToWin += 1
print(waysToWin)

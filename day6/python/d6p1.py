times = [int(x) for x in input().strip().split(":")[1].strip().split()]
distances = [int(x) for x in input().strip().split(":")[1].strip().split()]

total = 1
for t, d in zip(times, distances):
    waysToWin = 0
    for i in range(1,t+1):
        if (t-i)*i > d:
            waysToWin += 1
    total *= waysToWin
print(total)

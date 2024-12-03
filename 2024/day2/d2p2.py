def validMove(prev, next, increasing):
    if abs(next-prev) > 3 or abs(next-prev) < 1:
        return False
    return (increasing == None) or (increasing == (next > prev))

def isReportSafe(report):
    increasing = True if report[1] > report[0] else False
    for i in range(1, len(report)):
        if not validMove(report[i-1], report[i], increasing):
            return i
    return -1

numSafe = 0
while True:
    try:
        report = [int(x) for x in input().split()]
    except EOFError:
        break

    for i in range(len(report)):
        if isReportSafe(report[:i] + report[i+1:]) == -1:
            print(report)
            numSafe += 1
            break

print(numSafe)


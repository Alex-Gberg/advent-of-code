def calcArea(p1, p2):
    return abs(p1[0]-p2[0]+1) * abs(p1[1]-p2[1]+1)

points = []
while True:
    try:
        points.append([int(x) for x in input().split(',')])
    except EOFError:
        break

maxArea = -1
for p1 in points:
    for p2 in points:
        currArea = calcArea(p1, p2)
        maxArea = currArea if currArea > maxArea else maxArea

print(maxArea)
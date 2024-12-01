left, right = [], []

while True:
    try:
        l, r = [int(x) for x in input().split()]
        left.append(l)
        right.append(r)
    except EOFError:
        break

left.sort()
right.sort()

total_dist = 0
for l, r in zip(left, right):
    total_dist += abs(l - r)
print(total_dist)
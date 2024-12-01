from collections import defaultdict

left, right = [], []

while True:
    try:
        l, r = [int(x) for x in input().split()]
        left.append(l)
        right.append(r)
    except EOFError:
        break

counts = defaultdict(int)
for r in right:
    counts[r] += 1

similarity_score = 0
for l in left:
    if l in counts:
        similarity_score += l*counts[l]

print(similarity_score)

neighbors = dict()
while True:
    try:
        inp = input().split()
        neighbors[inp[0][:-1]] = inp[1:]
    except EOFError:
        break

found = 0
stack = neighbors['you']
while stack:
    node = stack.pop()
    if node == 'out':
        found += 1
        continue
    for n in neighbors[node]:
        stack.append(n)

print(found)
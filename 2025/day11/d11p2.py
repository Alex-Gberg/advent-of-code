neighbors = dict()
while True:
    try:
        inp = input().split()
        neighbors[inp[0][:-1]] = inp[1:]
    except EOFError:
        break

found = 0
stack = [(x, set()) for x in neighbors['svr']]
while stack:
    node = stack.pop()
    if node[0] == 'out': 
        if len(node[1]) == 2:
            found += 1
        continue
    newSet = node[1].copy()
    if node[0] == 'fft' or node[0] == 'dac':
        newSet.add(node[0])
    for n in neighbors[node[0]]:
        stack.append((n, newSet))

print(found)
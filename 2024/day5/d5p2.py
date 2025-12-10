from collections import defaultdict

must_follow = defaultdict(set)
while True:
    inp = input()
    if inp == '':
        break
    inp = [int(x) for x in inp.split('|')]
    must_follow[inp[0]].add(inp[1])

total_value = 0
while True:
    try:
        update = [int(x) for x in input().split(',')]
    except EOFError:
        break
    
    seen = set()
    correct = True
    i = 0
    while i < len(update):
        if not seen.isdisjoint(must_follow[update[i]]):
            correct = False
            seen.remove(update[i-1])
            update[i], update[i-1] = update[i-1], update[i]
            i -= 1
        else:
            seen.add(update[i])
            i += 1


    total_value += update[len(update)//2] if not correct else 0

print(total_value)
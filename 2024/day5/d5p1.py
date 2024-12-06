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
    value = update[len(update)//2]
    for i in range(len(update)):
        if not seen.isdisjoint(must_follow[update[i]]):
            value = 0
            break
        seen.add(update[i])

    total_value += value

print(total_value)
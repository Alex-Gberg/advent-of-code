from collections import defaultdict

stones = input().split()

length = len(stones)
blinks = 75

d = defaultdict(list)

def handle(i, val):
    d[i].append(val)
    global length
    if i > blinks:
        return
    if val == '0':
        handle(i+1, '1')
        return
    curr_length = len(val)
    if curr_length%2 == 0:
        length += 1
        handle(i+1, val[:curr_length//2])
        handle(i+1, val[curr_length//2:-1].lstrip('0') + val[-1])
    else:
        handle(i+1, str(int(val)*2024))

for s in stones:
    print(s)
    handle(1, s)
    
print(length)
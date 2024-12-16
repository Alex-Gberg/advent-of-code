stones = [int(x) for x in input().split()]

blinks = 25

for b in range(blinks):
    # print(b)
    # print(stones)
    replace = []
    for s in range(len(stones)):
        if stones[s] == 0:
            stones[s] = 1
        else:
            num_len = len(str(stones[s]))
            if num_len%2 == 0:
                split_len = num_len//2
                replace.append([s, stones[s] // (10**split_len), stones[s] % (10**split_len)])
            else:
                stones[s] *= 2024
    
    replaced = 0
    for r in replace:
        stones.insert(r[0]+replaced, r[2])
        stones.insert(r[0]+replaced, r[1])
        stones.pop(r[0]+2+replaced)
        replaced += 1

print(len(stones))
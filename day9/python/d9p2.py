inp = [int(x) for x in input().strip().split()]

def rec(l):
    if all([x == 0 for x in l]):
        return 0
    
    return l[0] - rec([l[i+1]-l[i] for i in range(len(l)-1)])

sum = 0
while inp:
    sum += rec(inp)

    try:
        inp = [int(x) for x in input().strip().split()]
    except EOFError:
        break

print(sum)
test = False
height = 103 if not test else 7
width = 101 if not test else 11
seconds = 100000

def print_grid(ps):
    for h in range(height):
        for w in range(width):
            if [w,h] in ps:
                print('#', end='')
            else:
                print('.', end='')
        print()

ps = []
vs = []
while True:
    try:
        p,v = [[int(y) for y in x[2:].split(',')] for x in input().split()]
        ps.append(p)
        vs.append(v)
    except EOFError:
        break

for s in range(seconds):
    standing = set()
    quadrant_count = dict({1: 0, 2: 0, 3:0, 4:0})
    for p in range(len(ps)):
        ps[p][0] = (ps[p][0] + vs[p][0])%width
        ps[p][1] = (ps[p][1] + vs[p][1])%height
        before = len(standing)
        standing.add((ps[p][0], ps[p][1]))
        if len(standing) - before > 0:
            if ps[p][0] < width//2:
                if ps[p][1] < height//2:
                    quadrant_count[1] += 1
                elif ps[p][1] > height//2:
                    quadrant_count[3] += 1
            elif ps[p][0] > width//2:
                if ps[p][1] < height//2:
                    quadrant_count[2] += 1
                elif ps[p][1] > height//2:
                    quadrant_count[4] += 1
    
    if quadrant_count[1] == quadrant_count[2] and quadrant_count[3] == quadrant_count[4] and quadrant_count[1] + quadrant_count[3] == quadrant_count[2] + quadrant_count[4]:
        print(s)
        print_grid(ps)

test = False
height = 103 if not test else 7
width = 101 if not test else 11
seconds = 1000

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
    print(s)
    for p in range(len(ps)):
        ps[p][0] = (ps[p][0] + vs[p][0])%width
        ps[p][1] = (ps[p][1] + vs[p][1])%height
    print_grid(ps)

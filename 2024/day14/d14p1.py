from functools import reduce
from operator import mul

test = False
height = 103 if not test else 7
width = 101 if not test else 11
seconds = 100
quadrant_count = dict({1: 0, 2: 0, 3:0, 4:0})

while True:
    try:
        p,v = [[int(y) for y in x[2:].split(',')] for x in input().split()]
    except EOFError:
        break
    
    dx, dy = v[0]*seconds, v[1]*seconds
    fx, fy = (p[0]+dx)%width, (p[1]+dy)%height
    
    if fx < width//2:
        if fy < height//2:
            quadrant_count[1] += 1
        elif fy > height//2:
            quadrant_count[3] += 1
    elif fx > width//2:
        if fy < height//2:
            quadrant_count[2] += 1
        elif fy > height//2:
            quadrant_count[4] += 1

print(reduce(mul, quadrant_count.values(), 1))
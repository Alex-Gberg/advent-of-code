beams = set([input().index('S')])

count = 0
while True:
    try:
        row = input()
        currBeams = set()
        for beam in beams:
            if row[beam] == '^':
                count += 1
                currBeams.add(beam-1)
                currBeams.add(beam+1)
            else:
                currBeams.add(beam)
        beams = currBeams
    except EOFError:
        break
print(count)
firstBeam = input().index('S')
graph = dict((0, firstBeam), [])
beams = set((0, firstBeam))

i = 1
while True:
    try:
        row = input()
        currBeams = set()
        for beam in beams:
            if row[beam[1]] == '^':
                beams[beam].append(i, beam[1])
                currBeams.add(beam-1)
                currBeams.add(beam+1)
            else:
                currBeams.add(beam)
        beams = currBeams
    except EOFError:
        break
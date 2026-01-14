while True:
    try:
        inp = input().split()
        lights = inp[0][1:-1]
        buttons = [set([int(y) for y in x[1:-1].split(',')]) for x in inp[1:-1]]
        
        
    except EOFError:
        break
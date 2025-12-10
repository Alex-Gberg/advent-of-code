pos = 50
count = 0
while True:
    try:
        instruction = input()
        dir, amp = instruction[0], int(instruction[1:])
        oldpos = pos
        count += amp // 100
        if dir == "R":
            pos = (pos + amp) % 100
            if pos < oldpos:
                count += 1
        else:
            pos = (pos - amp) % 100
            if oldpos != 0 and (pos == 0 or pos > oldpos):
                count += 1
        
    except EOFError:
        break
print(count)
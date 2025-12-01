pos = 50
count = 0
while True:
    try:
        instruction = input()
        dir, amp = instruction[0], int(instruction[1:])
        if dir == "R":
            pos = (pos + amp) % 100
        else:
            pos = (pos - amp) % 100
        
        if pos == 0:
            count += 1
    except EOFError:
        break
print(count)
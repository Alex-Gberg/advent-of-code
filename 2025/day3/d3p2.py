count = 0
while True:
    try:
        bank = [int(x) for x in input()]
        l = 0
        for i in range(11,-1,-1):
            value = max(bank[l:-1*i if i != 0 else None])
            count += pow(10, i) * value
            l += bank[l:].index(value) + 1
    except EOFError:
        break
print(count)
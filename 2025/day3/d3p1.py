count = 0
while True:
    try:
        bank = [int(x) for x in input()]
        count += (max(bank[:-1]) * 10) + max(bank[bank.index(max(bank[:-1]))+1:])
    except EOFError:
        break
print(count)
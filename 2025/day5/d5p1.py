ranges = []
while True:
    inp = input()
    if inp == '':
        break
    ranges.append([int(x) for x in inp.split('-')])

ingredients = []
while True:
    try:
        ingredients.append(int(input()))
    except EOFError:
        break

count = 0
for i in ingredients:
    for r in ranges:
        if r[0] <= i <= r[1]:
            count += 1
            break

print(count)
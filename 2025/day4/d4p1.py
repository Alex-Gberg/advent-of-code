diagram = []
while True:
    try:
        diagram.append(input())
    except EOFError:
        break

count = 0
for i in range(len(diagram)):
    for j in range(len(diagram[0])):
        if diagram[i][j] == '.':
            continue

        adjacent = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if 0 <= i+x < len(diagram) and 0 <= j+y < len(diagram[0]) and diagram[i+x][j+y] == '@':
                    adjacent += 1

        if adjacent < 5:
            count += 1
print(count)


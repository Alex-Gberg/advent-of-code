def solve(xres, yres, ax, ay, bx, by):
    b = (ax*yres - ay*xres)/(ax*by - ay*bx)
    a = (xres - bx*b)/ax
    return a,b

total_tokens = 0
while True:
    ax, ay = [int(x.split("+")[1].strip(",")) for x in input().split()[2:]]
    bx, by = [int(x.split("+")[1].strip(",")) for x in input().split()[2:]]
    x, y = [int(x.split("=")[1].strip(",")) for x in input().split()[1:]]

    a, b = solve(x, y, ax, ay, bx, by)
    if a%1 == 0 and b%1 == 0:
        total_tokens += 3*int(a) + int(b)

    try:
        input()
    except EOFError:
        break
print(total_tokens)
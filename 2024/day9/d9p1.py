map = input()

disk = [f for fx in [[i//2 if i%2 == 0 else -1 for y in range(int(x))] for i,x in enumerate(map)] for f in fx]

l, r = 0, len(disk)-1
checksum = 0
while l<=r:
    if disk[l] != -1:
        checksum += l*disk[l]
        l += 1
    else:
        while disk[r] == -1:
            r -= 1
        checksum += l*disk[r]
        l += 1
        r -= 1

print(checksum)
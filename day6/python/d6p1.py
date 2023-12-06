from math import sqrt, floor, ceil

times = [int(x) for x in input().strip().split(":")[1].strip().split()]
distances = [int(x) for x in input().strip().split(":")[1].strip().split()]

total = 1
for time, distance in zip(times, distances):
    det = sqrt(time**2-4*distance)
    total *= ceil(((-time - det)/-2)-1) - floor(((-time + det)/-2)+1) + 1
print(total)
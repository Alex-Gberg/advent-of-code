from math import sqrt, ceil, floor

time = int(''.join(input().strip().split(":")[1].strip().split()))
distance = int(''.join(input().strip().split(":")[1].strip().split()))

print(ceil(((-time - sqrt(time**2-4*distance))/-2)-1) - floor(((-time + sqrt(time**2-4*distance))/-2)+1) + 1)
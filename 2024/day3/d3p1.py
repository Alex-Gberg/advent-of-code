import re

with open('input', 'r') as input:
    print(sum([z[0] * z[1] for z in [[int(y) for y in x[4:-1].split(',')] for x in re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', input.read().replace('\n',''))]]))

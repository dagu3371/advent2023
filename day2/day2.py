import re
from functools import reduce
from collections import defaultdict
with open('input.txt', 'r') as file:
    lines = file.readlines()
pattern = re.compile(r'\s(\d+)\s*([a-zA-Z]+)')
res = 0
counter = 0
for line in lines:
    counter += 1
    # valid = True
    color_hash = defaultdict(int)
    # color_hash['red'] = 12
    # color_hash['green'] = 13
    # color_hash['blue'] = 14
    for l in line.split(';'):
        matches = re.findall(pattern, l)
        print(matches)
        for num, color in matches:
            color_hash[color] = max(color_hash[color], int(num))
            # if color_hash[color] < int(num):
            #     valid = False
    res += reduce(lambda x, y: x*y, color_hash.values())
    # if valid:
    #     res += counter
print(res)
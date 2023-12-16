schematic = []
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        schematic.append(list(line))
print(lines)
row = len(schematic)
col = len(schematic[0])
directions = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
number = ''
res = 0
valid = True
z = []
h = {}
for i in range(row):
    for j in range(col):
        if (j == 0 and number) or not schematic[i][j].isdigit():
            if not valid:
                if number:
                    # res += int(number)
                    if z[-1] not in h:
                        h[z[-1]] = []
                    h[z[-1]].append(number)
            number = ''
            valid = True
        else:
            number += schematic[i][j]
            for dx,dy in directions:
                if (i + dx) in range(row) and (j + dy) in range(col):
                    adj = schematic[i+dx][j+dy]
                    if adj != '.' and not adj.isdigit():
                        if adj == '*':
                            z.append((i+dx, j+dy))
                            valid = False
# print(res)
# print(z)
for v in h.values():
    if len(v) > 1:
        res += int(v[0]) * int(v[1])

print(res)
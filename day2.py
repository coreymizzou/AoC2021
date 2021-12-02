h = 0
d = 0
aim = 0

f = open('input.txt')
data = f.read().splitlines()

for line in data:
    movement, units = map(str, line.split(' '))
    if (movement == 'forward'):
        h += int(units)
        d = d + aim * int(units)
    elif (movement == 'up'):
        aim -= int(units)
    elif (movement == 'down'):
        aim += int(units)

position = d * h
print(position)

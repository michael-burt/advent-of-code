# part 1
with open("../input.txt") as input_file:
    input_str = input_file.read()
    lines = input_str.split('\n')

depth = 0
position = 0

for val in lines:
    if val.split(' ')[0] == 'forward':
        position += int(val.split(' ')[1])
    elif val.split(' ')[0] == 'up':
        depth -= int(val.split(' ')[1])
    elif val.split(' ')[0] == 'down':
        depth += int(val.split(' ')[1])
    else:
        break

print(f"part 1 answer = {depth * position}")

# part 2

depth = 0
position = 0
aim = 0

for val in lines:
    if val.split(' ')[0] == 'forward':
        position += int(val.split(' ')[1])
        depth += (int(val.split(' ')[1]) * aim)
    elif val.split(' ')[0] == 'up':
        aim -= int(val.split(' ')[1])
    elif val.split(' ')[0] == 'down':
        aim += int(val.split(' ')[1])
    else:
        break

print(f"part 2 answer = {depth * position}")

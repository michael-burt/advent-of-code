from copy import deepcopy

# part 1
with open("../input.txt") as input_file:
    input_str = input_file.read()
    horizontal_pos = [int(pos) for pos in input_str.strip().split(',')]

min_pos = min(horizontal_pos)
max_pos = max(horizontal_pos)
vals = [sum([abs(pos - i) for pos in horizontal_pos]) for i in range(min_pos, max_pos)]
print(f"part 1 answer = {min(vals)}")

range_vals = {0: 0,}
for i in range(1, max(horizontal_pos)+1):
    range_vals[i] = range_vals[i-1] + i

vals = [sum([range_vals[abs(pos - i)] for pos in horizontal_pos]) for i in range(min_pos, max_pos)]
print(f"part 2 answer = {min(vals)}")

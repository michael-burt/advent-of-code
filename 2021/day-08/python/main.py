# part 1
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g',]

with open("../input.txt") as input_file:
    input_str = input_file.read()
    lines = input_str.split('\n')

inputs = []

for line in lines[:-1]:
    parts = line.strip().split('|')[0].split() + line.strip().split('|')[1].split()
    inputs.append(parts)

counter = 0
for line in inputs:
    for out in line[1].strip().split():
        if len(out) in [2, 4, 3, 7]:
            counter += 1

print(f"part 1 answer = {counter}")

# part 2
input_sets = [[set(l) for l in line] for line in inputs]


def decoded(line):
    d = dict()

    # sort the inputs by length, compare sets
    for _s in sorted(line, key=len):
        if len(_s) == 2:
            d[1] = _s
        elif len(_s) == 3:
            d[7] = _s
        elif len(_s) == 4:
            d[4] = _s
        elif len(_s) == 5:
            if d[1].issubset(_s):
                d[3] = _s
            elif len(_s.intersection(d[4])) == 2:
                d[2] = _s
            elif len(_s.intersection(d[4])) == 3:
                d[5] = _s
        elif len(_s) == 6:
            if d[4].issubset(_s):
                d[9] = _s
            elif d[1].issubset(_s):
                d[0] = _s
            elif len(_s.intersection(d[1])) == 1:
                d[6] = _s
        elif len(_s) == 7:
            d[8] = _s

    answer = 0
    for idx, digit in enumerate(line[-4:]):
        _d = list(d.keys())[list(d.values()).index(digit)]
        answer += (10**abs(idx-3)) * _d

    return answer


p2_answer = 0
for idx, line in enumerate(input_sets):
    p2_answer += decoded([set(l) for l in line])

print(f"part 2 answer = {p2_answer}")

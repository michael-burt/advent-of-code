from copy import deepcopy

# part 1
with open("../input.txt") as input_file:
    input_str = input_file.read()
    fishies = [int(fish) for fish in input_str.strip().split(',')]

for day in range(0, 80):
    fishies = [fish - 1 for fish in fishies]
    for idx, fish in enumerate(fishies):
        if fish == -1:
            fishies[idx] = 6
            fishies.append(8)

print(f"part 1 answer: {len(fishies)}")

# part 2
with open("../input.txt") as input_file:
    input_str = input_file.read()
    fishies = [int(fish) for fish in input_str.strip().split(',')]

ages = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

for fish in fishies:
    ages[fish] += 1

for day in range(0, 256):
    ages_copy = deepcopy(ages)
    ages[8] = ages_copy[0]
    ages[7] = ages_copy[8]
    ages[6] = ages_copy[7] + ages_copy[0]
    ages[5] = ages_copy[6]
    ages[4] = ages_copy[5]
    ages[3] = ages_copy[4]
    ages[2] = ages_copy[3]
    ages[1] = ages_copy[2]
    ages[0] = ages_copy[1]

print(f"part 2 answer: {sum([v for k, v in ages.items()])}")

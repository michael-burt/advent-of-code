# part 1
with open("../input.txt") as input_file:
    input_str = input_file.read()
    lines = input_str.split('\n')

bits = len(lines[0].strip())
bit_counter = []
for i in range(0, bits):
    bit_counter.append({0: 0, 1: 0,})

for val in lines:
    for idx, i in enumerate(val):
        bit_counter[idx][int(i)] += 1

max_bits = ''.join([str(max(bit_position, key=bit_position.get)) for bit_position in bit_counter])
min_bits = ''.join([str(min(bit_position, key=bit_position.get)) for bit_position in bit_counter])
gamma = int(max_bits, 2)
epsilon = int(min_bits, 2)

print(f"part 1 answer = {epsilon * gamma}")

# part 2
bits_list = [val.strip() for val in lines if val != '']
bits_list_oxygen = bits_list
init_bits = bits_list

for i in range(0, bits):
    for line in init_bits:
        if len(init_bits) == 1:
            break
        if line.strip()[i] != max_bits[i]:
            try:
                init_bits.remove(line)
            except ValueError:
                pass

    bit_counter = []
    for i in range(0, bits):
        bit_counter.append({0: 0, 1: 0,})
    for line in init_bits:
        for idx, val in enumerate(line):
            bit_counter[idx][int(val)] += 1
    max_bits = ''.join([str(max(bit_position, key=bit_position.get)) for bit_position in bit_counter])

print(init_bits)

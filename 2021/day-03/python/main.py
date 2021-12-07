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
init_oxygen_bits = bits_list
init_co2_bits = bits_list

def filter_list_oxygen(idx, bits, ):
    positional_bit_list = [b[idx] for b in bits]
    d = {
        '0': len([b for b in positional_bit_list if b == '0']),
        '1': len([b for b in positional_bit_list if b == '1']),
    }
    out = []
    if d['1'] >= d['0']:
        for bit in bits:
            if bit[idx] == '1':
                out.append(bit)
    else:
        for bit in bits:
            if bit[idx] == '0':
                out.append(bit)
    return out

def filter_list_co2(idx, bits, ):
    positional_bit_list = [b[idx] for b in bits]
    d = {
        '0': len([b for b in positional_bit_list if b == '0']),
        '1': len([b for b in positional_bit_list if b == '1']),
    }
    out = []
    if d['1'] < d['0']:
        for bit in bits:
            if bit[idx] == '1':
                out.append(bit)
    else:
        for bit in bits:
            if bit[idx] == '0':
                out.append(bit)
    return out

for i in range(0, bits):
    if len(init_oxygen_bits) == 1:
        break
    else:
        init_oxygen_bits = filter_list_oxygen(i, init_oxygen_bits)

for i in range(0, bits):
    if len(init_co2_bits) == 1:
        break
    else:
        init_co2_bits = filter_list_co2(i, init_co2_bits)

oxygen = int(init_oxygen_bits[0], 2)
co2 = int(init_co2_bits[0], 2)
print(f"part 2 answer = {oxygen * co2}")

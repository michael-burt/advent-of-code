# part 1
with open("../input.txt") as input_file:
    input_str = input_file.read()
    lines = input_str.split('\n')

larger_than = 0
for idx, val in enumerate(lines):
    if val > lines[idx-1]:
        larger_than += 1

print(f"larger_than = {larger_than}")

# part 2
sliding_window = []
for idx, val in enumerate(lines):

    # break once we can no longer create window
    try:
        int(lines[idx+2])
    except ValueError:
        break

    window_value = sum([int(lines[idx+i]) for i in [0, 1, 2]])
    sliding_window.append(window_value)

window_larger_than = 0
for idx, val in enumerate(sliding_window):
    if val > sliding_window[idx-1]:
        window_larger_than += 1

print(f"window_larger_than = {window_larger_than}")

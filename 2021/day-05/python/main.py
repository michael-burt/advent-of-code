# part 1
with open("../input.txt") as input_file:
    input_str = input_file.read()
    lines = input_str.split('\n')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.danger = 0

    def inc_danger(self):
        self.danger += 1

# points = []
# for x in range (0, 1000):
#     for y in range(0, 1000):
#         points.append(Point(x, y))
#
# for idx, line in enumerate(lines[:-1]):
#     x1 = int(line.split(' -> ')[0].split(',')[0])
#     y1 = int(line.split(' -> ')[0].split(',')[1])
#     x2 = int(line.split(' -> ')[1].split(',')[0])
#     y2 = int(line.split(' -> ')[1].split(',')[1])
#     for point in [p for p in points if (p.x in [x1, x2]) or (p.y in [y1, y2])]:
#         if x1 == x2 == point.x:
#             if point.y <= max(y1, y2) and point.y >= min(y1, y2):
#                 point.inc_danger()
#         if y1 == y2 == point.y:
#             if point.x <= max(x1, x2) and point.x >= min(x1, x2):
#                 point.inc_danger()
#
# print(len([point.danger for point in points if point.danger > 1]))

# part 2
points = []
for x in range (0, 1000):
    for y in range(0, 1000):
        points.append(Point(x, y))

for idx, line in enumerate(lines[:-1]):
    x1 = int(line.split(' -> ')[0].split(',')[0])
    y1 = int(line.split(' -> ')[0].split(',')[1])
    x2 = int(line.split(' -> ')[1].split(',')[0])
    y2 = int(line.split(' -> ')[1].split(',')[1])
    for point in [p for p in points if ((max(x1, x2) >= p.x >= min(x1, x2)) and (max(y1, y2) >= p.y >= min(y1, y2)))]:
        if x1 == x2 == point.x:
            if point.y <= max(y1, y2) and point.y >= min(y1, y2):
                point.inc_danger()
        if y1 == y2 == point.y:
            if point.x <= max(x1, x2) and point.x >= min(x1, x2):
                point.inc_danger()
        if (abs(x1 - point.x) == abs(y1 - point.y)):
            point.inc_danger()

print(len([point.danger for point in points if point.danger > 1]))

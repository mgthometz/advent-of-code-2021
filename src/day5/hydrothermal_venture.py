from typing import DefaultDict


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Vents:
    def __init__(self) -> None:
        self.locations = DefaultDict(int)

    def add_line(self, p0, p1, include_diagonals=True) -> None:
        def calc_increment(coord0, coord1):
            if coord0 < coord1:
                return 1
            elif coord0 > coord1:
                return -1
            else:
                return 0
        x_inc = calc_increment(p0.x, p1.x)
        y_inc = calc_increment(p0.y, p1.y)
        if (x_inc != 0) and (y_inc != 0) and include_diagonals is False:
            return
        steps = max(abs(p0.x-p1.x), abs(p0.y-p1.y))
        x_start = p0.x
        y_start = p0.y
        x = x_start
        y = y_start
        for _ in range(steps+1):
            self.locations[(x, y)] += 1
            x += x_inc
            y += y_inc

    def count_dangerous(self) -> int:
        return sum([val > 1 for val in self.locations.values()])


with open('src/day5/input.txt') as f:
    coords = [[el.split(',') for el in l.rstrip().split(' -> ')]for l in f.readlines()]
    points = [(Point(int(c[0][0]), int(c[0][1])), Point(int(c[1][0]), int(c[1][1]))) for c in coords]

v1 = Vents()
v2 = Vents()
for p in points:
    v1.add_line(p[0], p[1], include_diagonals=False)
    v2.add_line(p[0], p[1], include_diagonals=True)

print("Part 1 (No Diagonals) Dangerous Vents Count:", v1.count_dangerous())
print("Part 2 Dangerous Vents Count:", v2.count_dangerous())

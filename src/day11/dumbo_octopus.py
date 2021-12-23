with open('src/day11/input.txt') as f:
    input = [[int(i) for i in list(l.strip())] for l in f.readlines()]


class Octopus:
    def __init__(self, level) -> None:
        self.level = level
        self.neighbors = []
        self.flashed = False
        self.flash_count = 0

    def add_neighbor(self, neighbor) -> None:
        self.neighbors.append(neighbor)

    def step(self) -> None:
        self.level += 1

    def increment(self) -> None:
        self.level += 1

    def flash(self) -> None:
        if (self.level >= 10) and self.flashed is False:
            self.flashed = True
            self.flash_count += 1
            for n in self.neighbors:
                n.increment()
                n.flash()

    def reset(self) -> None:
        if self.level >= 10:
            self.level = 0
            self.flashed = False


def get_adjacents(row, col, max_rows, max_cols):
    adjacents = []
    up_row = row - 1
    if up_row >= 0:
        adjacents.append((up_row, col))
    down_row = row + 1
    if down_row < max_rows:
        adjacents.append((down_row, col))
    left_col = col - 1
    if left_col >= 0:
        adjacents.append((row, left_col))
    right_col = col + 1
    if right_col < max_cols:
        adjacents.append((row, right_col))
    if up_row >= 0 and left_col >= 0:
        adjacents.append((up_row, left_col))
    if up_row >= 0 and right_col < max_cols:
        adjacents.append((up_row, right_col))
    if down_row < max_rows and left_col >= 0:
        adjacents.append((down_row, left_col))
    if down_row < max_rows and right_col < max_cols:
        adjacents.append((down_row, right_col))
    return adjacents


def create_grid(input):
    max_rows = len(input)
    max_cols = len(input[0])
    octopi = []
    for i in range(max_rows):
        cols = []
        for j in range(max_cols):
            cols.append(Octopus(input[i][j]))
        octopi.append(cols)
    # Add Neighbors
    for row in range(max_rows):
        for col in range(max_cols):
            current_oct = octopi[row][col]
            adjacent_idxs = get_adjacents(row, col, max_rows, max_cols)
            for adj in adjacent_idxs:
                current_oct.add_neighbor(octopi[adj[0]][adj[1]])
    return octopi


def count_flashes(octopi, n_steps):
    max_rows = len(octopi)
    max_cols = len(octopi[0])
    for _ in range(n_steps):
        for i in range(max_rows):
            for j in range(max_cols):
                octopi[i][j].step()
        for i in range(max_rows):
            for j in range(max_cols):
                octopi[i][j].flash()
        for i in range(max_rows):
            for j in range(max_cols):
                octopi[i][j].reset()
    return sum([oct.flash_count for row in octopi for oct in row])


def get_first_simultaneous(octopi):
    max_rows = len(octopi)
    max_cols = len(octopi[0])
    total_octopi = max_rows*max_cols
    step_count = 0
    while True:
        for i in range(max_rows):
            for j in range(max_cols):
                octopi[i][j].step()
        for i in range(max_rows):
            for j in range(max_cols):
                octopi[i][j].flash()
        step_count += 1
        simultaneous_cnt = sum([oct.flashed for row in octopi for oct in row])
        if total_octopi == simultaneous_cnt:
            return step_count
        for i in range(max_rows):
            for j in range(max_cols):
                octopi[i][j].reset()


def solve_p1(input):
    octopi = create_grid(input)
    total_flashes = count_flashes(octopi, n_steps=100)
    return total_flashes


def solve_p2(input):
    octopi = create_grid(input)
    first_sim = get_first_simultaneous(octopi)
    return first_sim


print("Part 1:", solve_p1(input))
print("Part 2:", solve_p2(input))

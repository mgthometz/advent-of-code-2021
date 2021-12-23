import math

with open('src/day9/input.txt') as f:
    input = [[int(i) for i in list(l.strip())] for l in f.readlines()]


def solve_p1(input):
    n_rows = len(input)
    n_cols = len(input[0])
    # searched = set()

    def up_higher(row, col, input):
        current = input[row][col]
        up_row = row - 1
        if up_row < 0:
            return True
        else:
            return current < input[up_row][col]

    def down_higher(row, col, input):
        current = input[row][col]
        down_row = row + 1
        if down_row >= n_rows:
            return True
        else:
            return current < input[down_row][col]

    def left_higher(row, col, input):
        current = input[row][col]
        left_col = col - 1
        if left_col < 0:
            return True
        else:
            return current < input[row][left_col]

    def right_higher(row, col, input):
        current = input[row][col]
        right_col = col + 1
        if right_col >= n_cols:
            return True
        else:
            return current < input[row][right_col]
    total_risk = 0
    for row_idx in range(n_rows):
        for col_idx in range(n_cols):
            if (up_higher(row_idx, col_idx, input) and 
                down_higher(row_idx, col_idx, input) and
                left_higher(row_idx, col_idx, input) and
                right_higher(row_idx, col_idx, input)):
                total_risk += input[row_idx][col_idx]+1
    return total_risk


def solve_p2(input):
    def recurse(location):
        if location in searched:
            return 0
        searched.add(location)
        value = input[location[0]][location[1]]
        if value == 9:
            return 0
        else:
            up = (location[0]-1, location[1])
            down = (location[0]+1, location[1])
            left = (location[0], location[1]-1)
            right = (location[0], location[1]+1)
            return 1 + recurse(up) + recurse(down) + recurse(left) + recurse(right)

    n_rows = len(input)
    n_cols = len(input[0])
    remaining = set([(row,col) for row in range(n_rows) for col in range(n_cols)])

    searched = set()
    # Add boundaries to searched
    searched.update([(-1, col) for col in range(n_cols)])
    searched.update([(row, -1) for row in range(n_rows)])
    searched.update([(n_rows, col) for col in range(n_cols)])
    searched.update([(row, n_cols) for row in range(n_rows)])

    basins = []
    while remaining:
        loc = remaining.pop()
        basin = recurse(loc)
        basins.append(basin)
        remaining.difference_update(searched)

    # Get three largest basins
    top3 = sorted(basins, reverse=True)[:3]
    return math.prod(top3)

print("Part 1:", solve_p1(input))
print("Part 2:", solve_p2(input))
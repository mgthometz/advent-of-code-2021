import numpy as np

with open('src/day10/input.txt') as f:
    input = [list(l.strip()) for l in f.readlines()]


pair_map = {'{': '}', '[': ']',
            '(': ')', '<': '>'}
closers = set(pair_map.values())


def find_illegal(line):
    line = line[::-1]
    c_stack = []
    while line:
        char = line.pop()
        if char in closers:
            if c_stack:
                expected = c_stack.pop()
                if expected == char:
                    continue
                else:
                    return char
            else:
                return char
        else:
            c_stack.append(pair_map[char])


def solve_p1(input):
    point_map = {')': 3, ']': 57,
                 '}': 1197, '>': 25137}
    points = []
    for line in input:
        illegal_char = find_illegal(line)
        if illegal_char:
            points.append(point_map[illegal_char])
        else:
            continue
    return sum(points)


def find_completions(line):
    line = line[::-1]
    c_stack = []
    while line:
        char = line.pop()
        if char in closers:
            c_stack.pop()
        else:
            c_stack.append(pair_map[char])
    return c_stack[::-1]


def solve_p2(input):
    point_map = {')': 1, ']': 2,
                 '}': 3, '>': 4}
    points = []
    for line in input:
        if find_illegal(line):
            continue
        completions = find_completions(line)
        score = 0
        for c in completions:
            score = score * 5 + point_map[c]
        points.append(score)
    return np.median(points)


print("Part 1 Solution:", solve_p1(input))
print("Part 2 Solution:", solve_p2(input))

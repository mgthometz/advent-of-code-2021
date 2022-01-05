import os
from collections import namedtuple

Paper = namedtuple('Paper', 'xmax ymax coordinates')

filename = os.path.join(os.path.dirname(__file__), "input.txt")
with open(filename) as f:
    lines = [line for line in f]
    coords = []
    xmax = 0
    ymax = 0
    for idx, l in enumerate(lines):
        cleaned = l.strip()
        if cleaned == '':
            break
        coord = [int(i) for i in cleaned.split(',')]
        xmax = max(xmax, coord[0])
        ymax = max(ymax, coord[1])
        coords.append(coord)

    p0 = Paper(xmax, ymax, coords)

    folds = []
    for line in lines[idx+1:]:
        cleaned = line.strip().split('=')
        cleaned = [cleaned[0][-1], int(cleaned[1])]
        folds.append(cleaned)


def fold_left(paper, fold_line):
    xmax0 = paper.xmax
    ymax0 = paper.ymax
    new_coords = []
    for coord in paper.coordinates:
        x0, y0 = coord[0], coord[1]
        if xmax0 - fold_line <= fold_line:
            if x0 < fold_line:
                x1 = x0
            else:
                x1 = 2 * fold_line - x0
        else:
            if x0 > fold_line:
                x1 = xmax0 - x0
            else:
                x1 = x0 + xmax0 - 2 * fold_line
        new_coord = (x1, y0)
        new_coords.append(new_coord)
    xmax1 = xmax0 - min(xmax0 - fold_line, fold_line) - 1
    paper_out = Paper(xmax1, ymax0, new_coords)
    return paper_out


def fold_up(paper, fold_line):
    xmax0 = paper.xmax
    ymax0 = paper.ymax
    new_coords = []
    for coord in paper.coordinates:
        x0, y0 = coord[0], coord[1]
        if ymax0 - fold_line <= fold_line:
            if y0 < fold_line:
                y1 = y0
            else:
                y1 = 2 * fold_line - y0
        else:
            if y0 > fold_line:
                y1 = ymax0 - y0
            else:
                y1 = y0 + ymax0 - 2 * fold_line
        new_coord = (x0, y1)
        new_coords.append(new_coord)
    ymax1 = ymax0 - min(ymax0 - fold_line, fold_line) - 1
    paper_out = Paper(xmax0, ymax1, new_coords)
    return paper_out


def fold(paper, folds):
    for fold in folds:
        fold_dir, fold_line = fold[0], fold[1]
        if fold_dir == 'x':
            paper = fold_left(paper, fold_line)
        else:
            paper = fold_up(paper, fold_line)
    return paper


def visualize(paper):
    grid = []
    for _ in range(paper.ymax+1):
        grid.append('.' * paper.xmax)
    for coord in paper.coordinates:
        x = coord[0]
        y = coord[1]
        grid[y] = grid[y][:x] + '#' + grid[y][x+1:]
    for line in grid:
        print(line)


def solve_p1(p0, folds):
    fold0 = [folds[0]]
    paper = fold(p0, fold0)
    return len(set(paper.coordinates))


def solve_p2(p0, folds):
    paper = fold(p0, folds)
    visualize(paper)


print("Part 1 Solution:", solve_p1(p0, folds))
print("Part 2 Solution:")
solve_p2(p0, folds)

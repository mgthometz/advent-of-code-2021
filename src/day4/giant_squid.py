from typing import DefaultDict


class BingoBoard:
    def __init__(self, number_grid):
        self.grid = number_grid
        n_rows = len(number_grid)
        n_cols = len(number_grid[0])
        # Create dictionay of board numbers and locations
        self.number_map = dict()
        for row_idx in range(n_rows):
            for col_idx in range(n_cols):
                self.number_map[number_grid[row_idx][col_idx]] = (row_idx, col_idx)
        self.matches = set()
        self.row_match_counter = DefaultDict(int)
        self.col_match_counter = DefaultDict(int)

    def check_draw(self, number):
        if number in self.number_map:
            self.matches.add(number)
            row_idx, col_idx = self.number_map[number]
            self.row_match_counter[row_idx] += 1
            self.col_match_counter[col_idx] += 1

    def is_winner(self):
        row_winner = 5 in self.row_match_counter.values()
        col_winner = 5 in self.col_match_counter.values()
        return row_winner or col_winner


with open('src/day4/input.txt') as f:
    lines = [l.rstrip() for l in f.readlines()]
    draws = [int(d) for d in lines[0].split(',')]
    boards = []
    for idx in range(2, len(lines)-2, 6):
        number_grid = [[int(el) for el in row.split()] for row in lines[idx:idx+5]]
        bb = BingoBoard(number_grid)
        boards.append(bb)


def ordered_winners(boards, draw):
    ''''
    Return tuple of list of winning boards and list of winning draws

    List of boards and list of draws in winning order
    '''
    winning_boards = []
    winning_draws = []
    remaining = boards
    for d in draws:
        remaining = []
        for b in boards:
            b.check_draw(d)
            if b.is_winner():
                winning_boards.append(b)
                winning_draws.append(d)
            else:
                remaining.append(b)
        boards = remaining
    return winning_boards, winning_draws


wbs, wds = ordered_winners(boards, draws)

first_result = sum([n for row in wbs[0].grid for n in row if n not in wbs[0].matches])*wds[0]
print("First Winner Result", first_result)
last_result = sum([n for row in wbs[-1].grid for n in row if n not in wbs[-1].matches])*wds[-1]
print("Last Winner Result", last_result)

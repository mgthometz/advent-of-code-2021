import os
import re


def vy0_bounds(y_l: int, y_u: int) -> list[int]:
    '''
    Lower bound equals y_l

    Upper bound equals max(-y_l, y_u)
    '''
    return [y_l, max(-y_l, y_u)]


def vx0_bounds(x_l: int, x_u: int, y_l: int, y_u: int) -> int:
    '''
    Lower bound is the minimum vx0 that satisfies:
    vx0 * (vx0 + 1) / 2 >= x_l

    Upper bound is x_u
    '''
    vx0_l = 1
    while True:
        if vx0_l * (vx0_l + 1) / 2 >= x_l:
            break
        else:
            vx0_l += 1
    vx0_u = x_u
    return [vx0_l, vx0_u]


def part1(y_l: int) -> int:
    return y_l*(y_l+1)/2


def part2(x_l: int, x_u: int, y_l: int, y_u: int) -> int:
    vy0_l, vy0_u = vy0_bounds(y_l, y_u)
    vx0_l, vx0_u = vx0_bounds(x_l, x_u, y_l, y_u)
    valid_inits = []
    for vx0 in range(vx0_l, vx0_u+1):
        for vy0 in range(vy0_l, vy0_u+1):
            x_t, y_t = 0, 0
            vx_t, vy_t = vx0, vy0
            while y_t >= y_l and x_t <= x_u:
                x_t += vx_t
                y_t += vy_t
                if x_t >= x_l and x_t <= x_u and y_t >= y_l and y_t <= y_u:
                    valid_inits.append([vx0, vy0])
                    break
                else:
                    vy_t -= 1
                    if vx_t > 0:
                        vx_t -= 1
                    elif vx_t < 0:
                        vx_t += 1
    return len(valid_inits)


if __name__ == '__main__':
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filename) as f:
        raw = [l.strip() for l in f][0]
    x_l, x_u = (int(i) for i in re.search(r'x=(-?\d+)\.*(-?\d+)', raw).group(1, 2))
    y_l, y_u = (int(i) for i in re.search(r'y=(-?\d+)\.*(-?\d+)', raw).group(1, 2))

    print("Part 1 Solution:", part1(y_l))
    print("Part 2 Solution:", part2(x_l, x_u, y_l, y_u))

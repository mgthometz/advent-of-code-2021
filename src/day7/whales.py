import numpy as np

with open('src/day7/input.txt') as f:
    positions = [int(i) for i in f.read().strip().split(',')]


def calc_total_loss(loss_fxn, data, parameter):
    loss = sum([loss_fxn(d, parameter) for d in positions])
    return loss


def l1_loss_fxn(point, parameter):
    return abs(point-parameter)


def part2_loss_fxn(point, parameter):
    # identity 1+2+..+n = n(n+1)/2
    n = abs(point - parameter)
    return n * (n + 1) / 2


def minimize_loss(loss_fxn, data, parameter_space):
    min_loss = float('inf')
    p_star = None  # Parameter that minimizes loss function
    for p in parameter_space:
        loss = calc_total_loss(loss_fxn, data, p)
        if loss < min_loss:
            min_loss = loss
            p_star = p
    return min_loss, p_star


# Brute Force search entire parameter space
parameter_space = range(min(positions), max(positions)+1)
part1_sol = minimize_loss(l1_loss_fxn, positions, parameter_space)

# Can prove median minimizes L1 loss
med = np.median(positions)
if type(med) is int:
    med_loss = calc_total_loss(l1_loss_fxn, positions, med)
else:
    med_loss = minimize_loss(l1_loss_fxn, positions, [np.floor(med), np.ceil(med)])

assert med_loss == part1_sol

part2_sol = minimize_loss(part2_loss_fxn, positions, parameter_space)
print("Part 1 Solution:", part1_sol[0])
print("Part 2 Solution:", part2_sol[0])

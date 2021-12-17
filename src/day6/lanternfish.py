with open('src/day6/input.txt') as f:
    initial = [int(i) for i in f.read().strip().split(',')]


def simulate_naive(initial, days):
    current = initial
    for _ in range(days):
        next = []
        for c in current:
            if c == 0:
                n = 6
                next.append(n)
                next.append(8)
            else:
                n = c - 1
                next.append(n)
        current = next
    return len(current)


def simulate_optimized(initial, days):
    fish_counts = [initial.count(i) for i in range(9)]
    for day in range(days):
        new_spawns = fish_counts.pop(0)
        fish_counts.append(new_spawns)
        fish_counts[6] += new_spawns
    return sum(fish_counts)


print("Part 1 Solution:", simulate_naive(initial=initial, days=80))
assert simulate_naive(initial=initial, days=80) == simulate_optimized(initial=initial, days=80)
print("Part 2 Solution:", simulate_optimized(initial=initial, days=256))

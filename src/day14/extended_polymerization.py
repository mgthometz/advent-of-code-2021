import os
from collections import Counter


filename = os.path.join(os.path.dirname(__file__), "input.txt")
with open(filename) as f:
    lines = [l.strip() for l in f]
    poly0 = list(lines[0].strip())
    rules = {}
    for line in lines[2:]:
        p, i = line.split(' -> ')
        rules[p] = i


def apply_rules_brute_force(polymer: list, steps: int) -> list:
    for _ in range(steps):
        new_polymer = []
        for idx in range(len(polymer)-1):
            pair = polymer[idx]+polymer[idx+1]
            insert = rules[pair]
            new_polymer.extend([polymer[idx], insert])
        new_polymer.append(polymer[-1])
        polymer = new_polymer
    most_common = Counter(new_polymer).most_common()
    return most_common[0][1] - most_common[-1][1]


def apply_rules_optimized(polymer: list, steps: int) -> list:
    chars = Counter(polymer)
    initial_pairs = Counter([''.join([a, b]) for a, b in zip(polymer, polymer[1:])])
    for _ in range(steps):
        final_pairs = Counter()
        for pair, count in initial_pairs.items():
            insert = rules[pair]
            chars[insert] += count
            final_pairs[pair[0]+insert] += count
            final_pairs[insert+pair[1]] += count
        initial_pairs = final_pairs
    most_common = chars.most_common()
    return most_common[0][1] - most_common[-1][1]

print("Solution Part 1:", apply_rules_brute_force(poly0, 10))
print("Solution Part 2:", apply_rules_optimized(poly0, 40))
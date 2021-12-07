with open('day3/input.txt') as f:
    binaries = [b.rstrip() for b in f]

### PART 1
### Determine product of gamma and epsilon
running_total = [0]*len(binaries[0])
for bin in binaries:
    for idx, bit in enumerate(bin):
        running_total[idx] += int(bit)
n_binaries = len(binaries)
## Compute gamma choosing most commin bit in ith position
gamma = [1  if tot > n_binaries/2 else 0 for tot in running_total]
##Convert bin to dec
gamma_b10 = sum([val*(2**idx) for idx, val in enumerate(gamma[::-1])])
## Compute epsilon by choosing least common bit in ith position
epsilon = [0  if tot > n_binaries/2 else 1 for tot in running_total]
##Convert bin to dec
epsilon_b10 = sum([val*(2**idx) for idx, val in enumerate(epsilon[::-1])])
print('Part 1 Answer:', gamma_b10*epsilon_b10)

###PART 2
#Determine product of o_rating and c_rating
n_bits = len(binaries[0])
o_candidates = set(binaries)
for b_idx in range(n_bits):
    if len(o_candidates)==1:
        break
    ones = set()
    zeros = set()
    for c in o_candidates:
        if int(c[b_idx])==1:
            ones.add(c)
        else:
            zeros.add(c)
    if len(ones)>=len(zeros):
        o_candidates = o_candidates.intersection(ones)
    else:
        o_candidates = o_candidates.intersection(zeros)

o_rating = o_candidates.pop()
o_rating_dec = sum([int(val)*(2**idx) for idx, val in enumerate(o_rating[::-1])])

c_candidates = set(binaries)
for b_idx in range(n_bits):
    if len(c_candidates)==1:
        break
    ones = set()
    zeros = set()
    for c in c_candidates:
        if int(c[b_idx])==1:
            ones.add(c)
        else:
            zeros.add(c)
    if len(ones) >= len(zeros):
        c_candidates = c_candidates.intersection(zeros)
    else:
        c_candidates = c_candidates.intersection(ones)
c_rating = c_candidates.pop()
c_rating_dec = sum([int(val)*(2**idx) for idx, val in enumerate(c_rating[::-1])])

print('Part 2 Answer:', o_rating_dec*c_rating_dec)
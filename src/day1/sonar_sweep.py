import os
print(os.getcwd())


with open('input.txt') as f:
    depths = [int(line.rstrip()) for line in f]

#PART 1 
print(sum([(b - a) > 0 for a, b in zip(depths, depths[1:])]))

#PART 2 SLIDING WINDOW
inc_cnt = 0
for idx in range(len(depths)-3):
    inc_cnt += depths[idx] < depths[idx+3]
print(inc_cnt)


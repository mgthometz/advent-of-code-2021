##PART 1
with open('day2/input.txt') as f:
    horizontal = 0
    depth = 0
    for command in f:
        cleaned = command.lstrip().split()
        direction = cleaned[0]
        magnitude = int(cleaned[1])
        if direction == 'forward':
            horizontal += magnitude
        elif direction == 'down':
            depth += magnitude
        elif direction == 'up':
            depth -= magnitude
        
print(depth*horizontal)

##PART 2
with open('day2/input.txt') as f:
    aim = 0
    depth = 0
    horizontal = 0
    for command in f:
        cleaned = command.rstrip().split()
        direction = cleaned[0]
        magnitude = int(cleaned[1])
        if direction == 'forward':
            horizontal += magnitude
            depth += magnitude * aim
        elif direction == 'up':
            aim -= magnitude
        elif direction == 'down':
            aim += magnitude
print(horizontal*depth)
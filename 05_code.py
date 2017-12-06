def maze_of_twisty_tramplines(jumps):
    steps = 0
    i = 0
    while i < len(jumps):
        next_jump = i + jumps[i]
        jumps[i] += 1
        i = next_jump
        steps += 1
    print steps

def part_2(jumps):
    steps = 0
    i = 0
    while i < len(jumps):
        next_jump = i + jumps[i]
        jumps[i] += -1 if jumps[i] >= 3 else 1
        i = next_jump
        steps += 1
    print steps


f = open('05_input.txt', 'r')
jumps = map(int, f.readlines())
f.close()

# Part 1
# maze_of_twisty_tramplines(jumps)

# Part 2
# part_2(jumps)


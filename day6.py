def memory_reallocation(blocks):
    redistribution = 0
    states = set()
    seen_state = False
    while not seen_state:
        distribute_memory = max(blocks)
        curr_index = blocks.index(distribute_memory) 
        blocks[curr_index] = 0

        while distribute_memory > 0:
            curr_index += 1
            blocks[curr_index % len(blocks)] += 1
            distribute_memory += -1

        redistribution += 1

        if tuple(blocks) not in states:
            states.add(tuple(blocks))
        else:
            seen_state = True 
    print redistribution

def part_2(blocks):
    redistribution = 0
    states = []
    seen_state = False
    while not seen_state:
        distribute_memory = max(blocks)
        curr_index = blocks.index(distribute_memory) 
        blocks[curr_index] = 0

        while distribute_memory > 0:
            curr_index += 1
            blocks[curr_index % len(blocks)] += 1
            distribute_memory += -1

        redistribution += 1

        if tuple(blocks) not in states:
            states.append(tuple(blocks))
        else:
            seen_state = True 
    print redistribution - states.index(tuple(blocks)) - 1


f = open('06_input.txt', 'r')
blocks = map(int, f.readline().split('\t'))

# Part 1
#memory_reallocation(blocks)

# Part 2
part_2(blocks)
